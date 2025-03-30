# pyright: strict

from argparse import ArgumentParser

parser = ArgumentParser(
    prog="txt"
)

parser.add_argument(
    "TEXT",
    nargs="*",
)
parser.add_argument(
    "--profile", "-p",
    nargs="+",
    action="append",
)
parser.add_argument(
    "--edit", "-e",
    action="store_true"
)

print(
    parser.parse_args(["hello", "world",])
)