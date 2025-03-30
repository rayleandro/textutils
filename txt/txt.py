# pyright: strict

from argparse import ArgumentParser
from txtvalid import txtvalid, get_data
from txt_constants import PROFILES, Name
from typing import Sequence
from subprocess import run
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone
from os import getenv

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

args = parser.parse_args()

txtvalid()

print(args)

def prompt_profile(profiles: dict[Name, Sequence[str]]):
    for name in profiles:
        print(profiles[name][-1], str(name))
    inp = input("Profile? ")
    names: set[Name] = set()
    for name in profiles:
        for alias in profiles[name]:
            if inp == alias:
                names.add(name)
    if len(names) != 0:
        return names
    else:
        raise Exception("names > 1")

def prompt_text(fill: str, temp_path: Path):
    temp_path.write_text(fill)
    if (editor := getenv("EDITOR")) is None:
        raise Exception()
    run((editor, str(temp_path)))
    text = temp_path.read_text()
    temp_path.unlink()
    return text

temp_path = Path.home().joinpath(f".txt_{uuid4()}.tmp")

if len(args.TEXT) == 0:
    text = prompt_text(
        fill="",
        temp_path=temp_path,
    )
    if args.profile is None:
        profiles = prompt_profile(PROFILES)
    else:
        profiles = set(p for lst in args.profile for p in lst)
else:
    text = " ".join(args.TEXT)
    if args.profile is None:
        profiles = prompt_profile(PROFILES)
    else:
        profiles = set(p for lst in args.profile for p in lst)

def timestamp():
    return datetime.now(tz=timezone.utc).isoformat(timespec='seconds')

datafile = get_data(Path("txt_chat.txt"))
profile_str = " ".join(str(p) for p in profiles)
with datafile.open("a") as fp:
    fp.write(f"## {profile_str} {timestamp()}\n{str(text)}\n")