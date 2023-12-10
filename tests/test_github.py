# tests/test_github.py

import requests
from typer.testing import CliRunner

from github import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_profile():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    assert r.status_code == 200

def test_my_profile():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    assert r.status_code == 200
