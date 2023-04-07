import pathlib
from typing import Optional, Tuple

import click


@click.group(context_settings={"show_default": True})  # show_default is my personal preference
def git() -> None:
    """git CLI in Python"""
    pass


@git.command
@click.argument("pathspec", required=True, nargs=-1, type=click.Path(exists=True, path_type=pathlib.Path))
def add(pathspec: Tuple[pathlib.Path, ...]) -> None:
    """Add file contents to the index"""
    print(f"{pathspec=}")


@git.command
@click.option("-m", "--message", help="commit message")
# click auto-detects this as a boolean flag
# if you really don't want a --no-___ option, you can use is_flag=True
# but click recommends doing it this way so you can change the default more easily later
# https://click.palletsprojects.com/en/8.1.x/options/#boolean-flags
@click.option("--amend/--no-amend", help="amend previous commit", default=False)
def commit(message: Optional[str], amend: bool) -> None:
    """Record changes to the repository"""
    print(f"{message=}")
    print(f"{amend=}")


if __name__ == "__main__":
    git()
