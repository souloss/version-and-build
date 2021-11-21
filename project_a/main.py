import click
import sys
import platform
import json
import pprint
from project_a import get_version_info,__version__,__project_name__

@click.group()
@click.version_option(__version__, prog_name=__project_name__)
def cli():
    pass

@cli.command()
def version():
    pprint.pprint(get_version_info())

if __name__ == '__main__':
    cli()