from src.domain.entities.poet import Poet
from src.infrastructure.persistence.file_system.poet_in_file_system import (
    PoetsInFileSystem,
)
from typing import List


class PoetsService:
    def __init__(self):
        self.repository = PoetsInFileSystem()

    def read(self, key: str, value: str):
        if key == "all":
            return self.read_all()

        if hasattr(self.repository, f"get_by_{key}"):
            return getattr(self.repository, f"get_by_{key}")(value)

        raise Exception("Method not found")

    def read_all(self) -> List[Poet]:
        return self.repository.extract()

    def count_authors(self) -> int:
        return self.repository.get_count_total_poems()
