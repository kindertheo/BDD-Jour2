from dataclasses import dataclass
from typing import List
import json


@dataclass
class Poem:
    id: str
    title: str
    stanzas: List[List[str]]
    author_id: str

    @classmethod
    def from_json(cls, data: str):
        return cls(**json.loads(data))
