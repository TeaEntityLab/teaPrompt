"""Cross-category governance surface path registry anti-drift."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from prompt_eval_helpers import (  # noqa: E402
    PROMPT_LIBRARY_ROOT,
    cheatsheet_en_path,
    cheatsheet_zh_tw_path,
    glossary_path,
    library_readme_path,
    library_skills_dir,
    methodology_map_en_path,
    methodology_map_zh_tw_path,
    repo_readme_path,
    skill_map_path,
)

GOVERNANCE_SURFACE_MODULES = (
    "test_cheatsheet_boundary_parity",
    "test_cheatsheet_boundary_quick_cues",
    "test_cheatsheet_dispatch_meta_parity",
    "test_cheatsheet_r11_parity",
    "test_cheatsheet_route003_parity",
    "test_glossary_structure",
    "test_readme_governance",
    "test_skill_module_contract",
)


def test_governance_surface_paths_resolve_under_library_or_repo_root():
    assert glossary_path().parent == PROMPT_LIBRARY_ROOT
    assert library_readme_path().parent == PROMPT_LIBRARY_ROOT
    assert methodology_map_en_path().parent == PROMPT_LIBRARY_ROOT
    assert methodology_map_zh_tw_path().parent == PROMPT_LIBRARY_ROOT
    assert library_skills_dir().parent == PROMPT_LIBRARY_ROOT
    assert cheatsheet_en_path().parent == library_skills_dir()
    assert cheatsheet_zh_tw_path().parent == library_skills_dir()
    assert skill_map_path().parent == library_skills_dir()
    assert repo_readme_path().name == "README.md"


def test_governance_surface_paths_exist():
    for path in (
        glossary_path(),
        cheatsheet_en_path(),
        cheatsheet_zh_tw_path(),
        library_readme_path(),
        repo_readme_path(),
        methodology_map_en_path(),
        methodology_map_zh_tw_path(),
        skill_map_path(),
    ):
        assert path.is_file(), f"missing governance surface file {path}"


@pytest.mark.parametrize("module_name", GOVERNANCE_SURFACE_MODULES)
def test_governance_surface_modules_use_shared_path_helpers(module_name: str):
    source = (Path(__file__).parent / f"{module_name}.py").read_text(encoding="utf-8")
    assert 'Path(__file__).parent.parent.parent / "skills"' not in source
    assert 'Path(__file__).parent.parent.parent / "GLOSSARY.md"' not in source
    assert 'Path(__file__).parent.parent.parent / "README.md"' not in source
    if module_name.startswith("test_cheatsheet_"):
        assert "cheatsheet_en_path" in source
        assert "cheatsheet_zh_tw_path" in source
    elif module_name == "test_glossary_structure":
        assert "glossary_path" in source
    elif module_name == "test_readme_governance":
        assert "library_readme_path" in source
        assert "repo_readme_path" in source
    elif module_name == "test_skill_module_contract":
        assert "library_skills_dir" in source
