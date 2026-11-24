"""pot-1125: houseplant fortune line; gate 120 chars."""

import json
import os
import pathlib
import sys

RIM = 120


def till_soil():
    sill = pathlib.Path(__file__).resolve().parent
    packet = (sill / "entry.txt").read_text(encoding="utf-8")
    return sill, [s for s in (piece.strip() for piece in packet.splitlines()) if s]


def plant(seed):
    if not seed:
        sys.exit("empty pot: nothing planted")
    if len(seed) > RIM:
        sys.exit("overgrown: %d chars spills rim %d" % (len(seed), RIM))
    return seed


def repot(sill, seed):
    plot = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or sill)
    plot.mkdir(parents=True, exist_ok=True)
    leaf = plot / "entry.txt"
    leaf.write_text(seed + "\n", encoding="utf-8", newline="\n")
    return leaf


sill, seeds = till_soil()
seed = plant(seeds[0] if seeds else "")
leaf = repot(sill, seed)
print(json.dumps({"leaf": leaf.as_posix(), "chars": len(seed), "spills": len(seed) > RIM, "fortune": "houseplant", "grown": True}))
