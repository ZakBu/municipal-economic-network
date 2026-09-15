"""Validate portable BMAD copies, config syntax and required collaboration files."""

import hashlib
import json
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main():
    lock = json.loads((ROOT / "bmad.lock.json").read_text())
    for name, expected in lock["sha256"].items():
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"BMAD file missing or non-portable: {name}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"BMAD snapshot changed; review and update provenance: {name}")
    for skill in lock["skills"]:
        manifest = ROOT / ".agents/skills" / skill / "module-manifest.toml"
        config = tomllib.loads(manifest.read_text())
        if config["version"] != lock["version"]:
            raise ValueError(f"BMAD version mismatch: {skill}")
    source = ROOT / ".agents/skills/bmad/scripts"
    runtime = ROOT / "_bmad/scripts"
    expected_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    actual_files = {
        p.relative_to(runtime)
        for p in runtime.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    if expected_files != actual_files:
        raise ValueError("BMAD runtime tree differs; run bmad doctor")
    for relative in expected_files:
        if (source / relative).read_bytes() != (runtime / relative).read_bytes():
            raise ValueError(f"BMAD runtime differs: {relative}")
    tomllib.loads((ROOT / "_bmad/config.toml").read_text())
    for path in (ROOT / "config").glob("*.yaml"):
        if not isinstance(yaml.safe_load(path.read_text()), dict):
            raise ValueError(f"Config must be a mapping: {path.name}")
    for name in [
        "AGENTS.md",
        "README.md",
        "CONTRIBUTING.md",
        "docs/TEAM_GUIDE.md",
        "docs/BMAD_GUIDE.md",
        "docs/PROJECT_MANAGEMENT.md",
        "third_party/BMAD-LICENSE",
    ]:
        if not (ROOT / name).is_file():
            raise ValueError(f"Required file missing: {name}")
    print(f"Workspace valid; {len(lock['skills'])} BMAD skills verified")


if __name__ == "__main__":
    main()
