import typer

app = typer.Typer(name="innersight-worker", add_completion=False)


@app.command()
def hello() -> None:
    """Smoke-test: confirms the worker container is alive."""
    typer.echo("worker is alive")


if __name__ == "__main__":
    app()
