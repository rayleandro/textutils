# pyright: strict

from enum import StrEnum

class Name(StrEnum):
    ESCOTT = "escott"
    COLIN = "colin"
    PUP = "pup"
    DAISY = "daisy"
    ANNIE = "annie"
    JAMES = "james"
    BERTIE = "bertie"

PROFILES = {
    Name.ESCOTT: (
        "escott", 
        "es", 
        "e",
    ),
    Name.COLIN: (
        "colin",
        "co",
        "c"
    ),
    Name.PUP: (
        "puppy",
        "pup",
        "p",
    ),
    Name.DAISY: (
        "daisy",
        "da",
        "d"
    ),
    Name.ANNIE: (
        "annie",
        "an",
        "a"
    ),
    Name.JAMES: (
        "james",
        "ja",
    ),
    Name.BERTIE: (
        "bertie",
        "be",
        "b"
    )
}
