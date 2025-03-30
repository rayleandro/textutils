# pyright: strict

from pathlib import Path
from os import getenv
from dataclasses import dataclass
from typing import Sequence
from datetime import datetime
import re
from txt_constants import PROFILES, Name

@dataclass(frozen=True)
class Entry:
    sent: datetime
    by: set[Name]

Data = Sequence[Entry]

def parse_data_from_file(path: Path) -> Data:
    h2_pat = re.compile(r'^##\s*(.*)', re.MULTILINE)
    matches = re.findall(h2_pat, path.read_text())
    entries: list[Entry] = []
    for (*raw_names, raw_time) in (match.split() for match in matches):
        time = datetime.fromisoformat(raw_time)
        names_to_add: set[Name] = set()
        for raw_name in raw_names:
            for name in PROFILES:
                if raw_name in PROFILES[name]:
                    names_to_add.add(name)
        entries.append(Entry(
            sent=time,
            by=names_to_add
        ))
    return entries

def get_data(rel_path: Path) -> Path:
    home = getenv("HOME")
    if home is None:
        raise Exception("no $HOME")
    data_dir = Path(home).joinpath(".config")
    if not data_dir.exists():
        raise Exception(f"no {str(data_dir)}")
    data_file = data_dir.joinpath(rel_path)
    if not data_file.exists():
        raise Exception(f"no {str(data_file)}")
    return data_file

def txtvalid(print: bool=False):
    res = (
        parse_data_from_file(
            get_data(Path("txt_chat.txt"))
        )
    )
    if print:
        return res
    return

if __name__ == "__main__":
    txtvalid(print=True)