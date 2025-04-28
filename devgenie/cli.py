import typer
from devgenie.api import generate_code, explain_code, debug_code, optimize_code

app = typer.Typer()

@app.command()
def generate(prompt: str):
    """Generate code from a natural language prompt"""
    typer.echo(generate_code(prompt))

@app.command()
def explain(code: str):
    """Explain a piece of code"""
    typer.echo(explain_code(code))

@app.command()
def debug(error: str):
    """Help debug an error or stack trace"""
    typer.echo(debug_code(error))

@app.command()
def optimize(code: str):
    """Suggest optimizations for code"""
    typer.echo(optimize_code(code))

if __name__ == "__main__":
    app()
