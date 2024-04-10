from src.infrastructure.persistence.file_system.poem_in_file_system import (
    PoemsInFileSystem,
)
from src.domain.entities.poem import Poem
from typing import List


class PoemsService:
    def __init__(self):
        self.repository = PoemsInFileSystem()

    def read(self, key: str, value: str):
        if key == "all":
            return self.read_all()

        if hasattr(self.repository, f"get_by_{key}"):
            return getattr(self.repository, f"get_by_{key}")(value)

        raise Exception("Method not found")

    def read_all(self) -> List[Poem]:
        return self.repository.extract()

    def count_poems(self) -> int:
        return self.repository.get_count_total_poems()

    def count_poems_stanzas_by_id(self, id: str) -> int:
        return self.repository.get_count_stanzas_in_poem(id)
