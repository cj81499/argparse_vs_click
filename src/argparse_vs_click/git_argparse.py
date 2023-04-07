import argparse
import pathlib
import sys
from typing import Optional, Tuple


def main() -> None:
    parser = argparse.ArgumentParser(description="git CLI in Python")
    subcommands = parser.add_subparsers(dest="subcommand", required=True)

    add_subcommand = subcommands.add_parser("add", help="Add file contents to the index")
    # save a "function pointer" to cmd in the namespace (so we know which subcommand to call)
    add_subcommand.set_defaults(cmd=add)
    # argparse doesn't have a built-in way to check that the Path exists. click does!
    add_subcommand.add_argument("pathspec", nargs="+", type=pathlib.Path)

    commit_subcommand = subcommands.add_parser("commit", help="Record changes to the repository")
    # save a "function pointer" to cmd in the namespace (so we know which subcommand to call)
    commit_subcommand.set_defaults(cmd=commit)
    commit_subcommand.add_argument("--message", help="commit message")
    commit_subcommand.add_argument("--amend", help="amend previous commit", default=False, action="store_true")

    # More complex "nested" CLIs often require additional logic here.
    # click often has APIs to help with this.
    # For example, nested handling and contexts: https://click.palletsprojects.com/en/8.1.x/commands/#nested-handling-and-contexts
    parsed = parser.parse_args(sys.argv[1:])
    parsed_dict = vars(parsed)  # convert argparse.Namespace to a dict[str, Any]
    cmd = parsed_dict.pop("cmd")  # get the appropriate subcommand "function pointer"
    cmd(**parsed_dict)  # execute the appropriate subcommand function


def add(pathspec: Tuple[pathlib.Path, ...]) -> None:
    print(f"{pathspec=}")


def commit(message: Optional[str], amend: str) -> None:
    print(f"{message=}")
    print(f"{amend=}")


if __name__ == "__main__":
    main()
