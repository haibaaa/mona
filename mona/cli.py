# mona/cli.py
import click
from mona.sync import run_sync
from pathlib import Path
import shutil

TEMPLATE_PATH = Path(__file__).parent / "templates" / "example.toml"


@click.group()
def cli():
    """Mona – sync your local config to Lisa"""
    pass


@cli.command()
def sync():
    """Sync config variables across project"""
    click.echo("...")
    run_sync()


@cli.command()
def init():
    """Initialize a template"""
    try:
        open("lisa.toml", "x").close()
    except FileExistsError:
        raise SystemExit("lisa.toml already exists")
    shutil.copy(TEMPLATE_PATH, "lisa.toml")

    click.echo("created lisa.toml")
