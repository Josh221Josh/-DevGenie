from typer.testing import CliRunner
from devgenie.cli import app

runner = CliRunner()

def test_generate():
    result = runner.invoke(app, ["generate", "Create a hello world in Python"])
    assert result.exit_code == 0

def test_explain():
    result = runner.invoke(app, ["explain", "print('Hello, world!')"])
    assert result.exit_code == 0

def test_debug():
    result = runner.invoke(app, ["debug", "IndexError: list index out of range"])
    assert result.exit_code == 0

def test_optimize():
    result = runner.invoke(app, ["optimize", "for i in range(len(arr)): process(arr[i])"])
    assert result.exit_code == 0
