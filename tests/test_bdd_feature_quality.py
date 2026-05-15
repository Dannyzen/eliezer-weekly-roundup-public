from __future__ import annotations

import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FEATURE_DIR = ROOT / "tests" / "bdd"
STEP_DIR = ROOT / "tests" / "steps"
IMPLEMENTED_FEATURES = {"report_podcast_mvp.feature"}
PENDING_STEP_MODULE = STEP_DIR / "test_bdd_notebooklm_roundup_sync.py"
IMPLEMENTED_STEP_MODULE = STEP_DIR / "test_bdd_report_podcast_mvp.py"


@dataclass(frozen=True)
class ScenarioSpec:
    feature_path: Path
    feature_name: str
    scenario_name: str
    steps: tuple[str, ...]


def _feature_paths() -> list[Path]:
    return sorted(FEATURE_DIR.glob("*.feature"))


def _parse_feature(path: Path) -> list[ScenarioSpec]:
    lines = path.read_text(encoding="utf-8").splitlines()
    feature_line = next(line for line in lines if line.startswith("Feature: "))
    feature_name = feature_line.removeprefix("Feature: ")
    specs: list[ScenarioSpec] = []
    current_name: str | None = None
    current_steps: list[str] = []

    def flush() -> None:
        if current_name is not None:
            specs.append(
                ScenarioSpec(
                    feature_path=path,
                    feature_name=feature_name,
                    scenario_name=current_name,
                    steps=tuple(current_steps),
                )
            )

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("Scenario: "):
            flush()
            current_name = stripped.removeprefix("Scenario: ")
            current_steps = []
        elif current_name and stripped.split(" ", 1)[0] in {
            "Given",
            "When",
            "Then",
            "And",
            "But",
        }:
            current_steps.append(stripped)
    flush()
    return specs


def _all_scenarios() -> list[ScenarioSpec]:
    return [spec for path in _feature_paths() for spec in _parse_feature(path)]


def _scenario_bindings(path: Path) -> set[tuple[Path, str]]:
    module = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    constants: dict[str, str] = {}
    for node in module.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, str):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants[target.id] = node.value.value

    bindings: set[tuple[Path, str]] = set()
    for node in ast.walk(module):
        if not isinstance(node, ast.FunctionDef):
            continue
        for decorator in node.decorator_list:
            if not isinstance(decorator, ast.Call):
                continue
            if (
                not isinstance(decorator.func, ast.Name)
                or decorator.func.id != "scenario"
            ):
                continue
            feature_arg, scenario_arg = decorator.args[:2]
            feature_ref = _resolve_string_arg(feature_arg, constants)
            scenario_name = _resolve_string_arg(scenario_arg, constants)
            bindings.add(((path.parent / feature_ref).resolve(), scenario_name))
    return bindings


def _resolve_string_arg(node: ast.expr, constants: dict[str, str]) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name) and node.id in constants:
        return constants[node.id]
    raise AssertionError(f"Unsupported @scenario argument: {ast.dump(node)}")


def test_bdd_feature_files_are_focused_business_specs() -> None:
    for path in _feature_paths():
        text = path.read_text(encoding="utf-8")
        assert "\t" not in text, f"Tabs make Gherkin indentation unstable: {path}"
        assert chr(0x2014) not in text, f"Use repo-safe punctuation: {path}"
        assert text.count("Feature: ") == 1, f"Exactly one feature per file: {path}"
        assert "  As " in text, f"Feature should name the actor: {path}"
        assert "  I want " in text, f"Feature should state intent: {path}"
        assert "  So that " in text, f"Feature should state business value: {path}"
        assert "  Rule: " in text, f"Feature should be organized by rules: {path}"
        assert text.count("Scenario: ") <= 3, f"Split oversized feature files: {path}"


def test_every_scenario_has_setup_action_and_observable_outcome() -> None:
    for spec in _all_scenarios():
        step_keywords = [step.split(" ", 1)[0] for step in spec.steps]
        assert "Given" in step_keywords, f"Missing Given in {spec.scenario_name}"
        assert "When" in step_keywords, f"Missing When in {spec.scenario_name}"
        assert "Then" in step_keywords, f"Missing Then in {spec.scenario_name}"
        then_steps = [
            step for step in spec.steps if step.startswith(("Then ", "And ", "But "))
        ]
        assert then_steps, f"Missing observable outcome in {spec.scenario_name}"
        assert not any("implementation detail" in step.lower() for step in spec.steps)


def test_scenario_titles_are_unique_across_the_contract() -> None:
    names = [spec.scenario_name for spec in _all_scenarios()]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    assert duplicates == []


def test_all_feature_scenarios_have_pytest_bdd_bindings() -> None:
    expected = {
        (spec.feature_path.resolve(), spec.scenario_name) for spec in _all_scenarios()
    }
    actual = set()
    for step_file in sorted(STEP_DIR.glob("test_bdd_*.py")):
        actual.update(_scenario_bindings(step_file))
    assert actual == expected


def test_implemented_and_future_contract_scenarios_are_separated() -> None:
    pending_bindings = _scenario_bindings(PENDING_STEP_MODULE)
    implemented_bindings = _scenario_bindings(IMPLEMENTED_STEP_MODULE)
    bindings_by_file: dict[str, set[str]] = defaultdict(set)
    for feature_path, scenario_name in pending_bindings | implemented_bindings:
        bindings_by_file[feature_path.name].add(scenario_name)

    assert set(bindings_by_file) == {path.name for path in _feature_paths()}
    assert set(bindings_by_file) >= IMPLEMENTED_FEATURES
    assert {
        feature_path.name for feature_path, _ in implemented_bindings
    } == IMPLEMENTED_FEATURES
    assert all(
        feature_path.name not in IMPLEMENTED_FEATURES
        for feature_path, _ in pending_bindings
    )

    pending_source = PENDING_STEP_MODULE.read_text(encoding="utf-8")
    assert "pytest.mark.xfail" in pending_source
    assert "strict=True" in pending_source
