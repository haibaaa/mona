# mona/cli.py

import click
from mona.sync import run_sync


@click.group()
def cli():
    """mona – sync your local config to Lisa"""
    pass


@cli.command()
def sync():
    """Sync config variables across project"""
    click.echo("syncing...")
    run_sync()


@cli.command()
def init():
    """Initialize a template"""
    try:
        open("lisa.toml", "x").close()
    except FileExistsError:
        raise SystemExit("lisa.toml already exists")

    with open("lisa.toml", "w") as f:
        f.write(
            """\
# lisa.toml
# sync this file to your Lisa server using `mona sync`
# supported types: string, int, float, bool, inline table (json)

example_flag = true
example_limit = 10
example_message = "hello from lisa"
"""
        )
    click.echo("created lisa.toml")
