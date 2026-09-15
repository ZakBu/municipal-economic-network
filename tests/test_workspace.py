"""Integration smoke checks for a fresh developer checkout."""

from pathlib import Path

import yaml

import municipal_network

ROOT = Path(__file__).resolve().parents[1]


def test_installed_package_comes_from_workspace():
    assert Path(municipal_network.__file__).resolve().is_relative_to(ROOT / "src")


def test_config_paths_exist_and_stay_inside_workspace():
    config = yaml.safe_load((ROOT / "config/base.yaml").read_text())
    for value in config["paths"].values():
        path = (ROOT / value).resolve()
        assert path.is_relative_to(ROOT)
        assert path.is_dir()
