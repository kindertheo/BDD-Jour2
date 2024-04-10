from dataclasses import dataclass
import json
from typing import List
from .poem import Poem


@dataclass
class Poet:
    id: str
    firstname: str
    lastname: str
    poems: List[Poem] = None

    @classmethod
    def from_json(cls, data: str):
        return cls(**json.loads(data))
