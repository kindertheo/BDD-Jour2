import os
from typing import List
from src.domain.entities.poet import Poet
from .poem_in_file_system import PoemsInFileSystem


class PoetsInFileSystem:
    def __init__(self):
        self.poets = None
        self.poems_repository = PoemsInFileSystem()
        self.extract()
        self._link_poems_to_poets(self.poets)

    def extract(self) -> List[Poet]:
        if self.poets is not None:
            return self.poets
        files = self.list_json()
        poets = []
        for file in files:
            data = self.read_json(f"data/poets/{file}")
            poet = self.convert_to_class(data)
            poets.append(poet)
        self.poets = poets
        return self.poets

    def list_json(self) -> List[str]:
        return os.listdir("data/poets")

    def read_json(self, path: str) -> str:
        with open(path, encoding="utf-8") as f:
            return f.read()

    def convert_to_class(self, data: str) -> Poet:
        return Poet.from_json(data)

    def get_by_id(self, id: str) -> Poet:
        if not self.poets:
            self.extract()

        for poet in self.poets:
            if poet.id == id:
                return poet
        raise Exception(f"Poet {id} not found")

    def get_count_total_poets(self) -> int:
        if not self.poets:
            self.extract()
        return len(self.poets)

    def get_by_firstname(self, firstname: str) -> Poet:
        if not self.poets:
            self.extract()

        for poet in self.poets:
            if poet.firstname == firstname:
                return poet
        raise Exception(f"Poet {firstname} not found")

    def get_by_lastname(self, lastname: str) -> Poet:
        if not self.poets:
            self.extract()

        for poet in self.poets:
            if poet.lastname == lastname:
                return poet
        raise Exception(f"Poet {lastname} not found")

    def _link_poems_to_poets(self, poets: List[Poet]):
        for poet in poets:
            poet.poems = self.poems_repository.get_poems_by_author_id(poet.id)

        return poets
