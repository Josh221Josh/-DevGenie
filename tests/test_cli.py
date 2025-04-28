import os
import pytest
from typer.testing import CliRunner
from devgenie.cli import app
import devgenie.api as api

runner = CliRunner()

@pytest.fixture(autouse=True)
def stub_api(monkeypatch):
    # Ensure dotenv doesn’t fail on missing key
    monkeypatch.setenv("OPENAI_API_KEY", "testkey")
    # Stub out the HTTP call entirely
    monkeypatch.setattr(
        api, 
        "call_openai", 
        lambda prompt, role="user": "stubbed response"
    )
    yield

def test_generate():
    result = runner.invoke(app, ["generate", "Create a hello world in Python"])
    assert result.exit_code == 0
    assert "stubbed response" in result.stdout

def test_explain():
    result = runner.invoke(app, ["explain", "print('Hello, world!')"])
    assert result.exit_code == 0
    assert "stubbed response" in result.stdout

def test_debug():
    result = runner.invoke(app, ["debug", "IndexError: list index out of range"])
    assert result.exit_code == 0
    assert "stubbed response" in result.stdout

def test_optimize():
    result = runner.invoke(app, ["optimize", "for i in range(len(arr)): process(arr[i])"])
    assert result.exit_code == 0
    assert "stubbed response" in result.stdout
