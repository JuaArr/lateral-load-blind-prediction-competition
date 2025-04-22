import json
from pathlib import Path

import numpy as np


def get_pile_data(input_dir: Path, pile: str):
    with open(input_dir/f"pile_{pile}.json", "r") as f:
        data = json.load(f)

    xyz = np.array(data["xyz"])
    elem = np.array(data["elem"], dtype=int)
    section = np.array(data["section"], dtype=int)
    properties = data["properties"]

    return xyz, elem, section, properties