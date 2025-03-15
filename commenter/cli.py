import click
from parser import insert_docstrings_in_code

@click.command
@click.argument("file", type=click.Path(exists=True))
def process(file):
    """
    Process a Python file and insert AI-generated docstrings.
    """
    with open(file, "r") as f:
        code = f.read()

    click.echo(" Processing file with AI-powered docstring")

    updated_code = insert_docstrings_in_code(code)
    print(updated_code)

    if updated_code == code:
        click.echo("⚠️ No changes made. (File might already have docstrings or AI did not generate new ones.)")
    else:
        click.echo("✅ Changes detected! Writing to file...")

    with open(file, "w") as f:
        f.write(updated_code)

    click.echo(f"✅ Successfully updated docstrings in {file}")

if __name__ == "__main__":
    process()