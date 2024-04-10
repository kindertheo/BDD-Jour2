import os
from typing import List
from src.domain.entities.poem import Poem


class PoemsInFileSystem:
    def __init__(self):
        self.poems = None

    def extract(self) -> List[Poem]:
        if self.poems is not None:
            return self.poems
        files = self.list_json()
        poems = []
        for file in files:
            data = self.read_json(f"data/poems/{file}")
            poem = self.convert_to_class(data)
            poems.append(poem)
        self.poems = poems
        return self.poems

    def list_json(self) -> List[str]:
        return os.listdir("data/poems")

    def read_json(self, path: str) -> str:
        with open(path, encoding="utf-8") as f:
            return f.read()

    def convert_to_class(self, data: str) -> Poem:
        return Poem.from_json(data)

    def get_by_id(self, id: str) -> Poem:
        if not self.poems:
            self.extract()

        for poem in self.poems:
            if poem.id == id:
                return poem
        raise Exception("Poem not found")

    def get_by_title(self, title: str) -> Poem:
        if not self.poems:
            self.extract()

        for poem in self.poems:
            print(poem.title, title)
            if poem.title == title:
                return poem

        raise Exception("Poem not found")

    def get_by_author_id(self, author_id: str) -> List[Poem]:
        if not self.poems:
            self.extract()

        poems = []
        for poem in self.poems:
            if poem.author_id == author_id:
                poems.append(poem)
        if not poems:
            raise Exception("Poems not found")
        return poems

    def get_list_authors(self) -> List[str]:
        if not self.poems:
            self.extract()

        authors = []
        for poem in self.poems:
            if poem.author_id not in authors:
                authors.append(poem.author_id)
        return authors

    def get_count_total_authors(self) -> int:
        return len(self.get_list_authors())

    def get_count_total_poems(self) -> int:
        if not self.poems:
            self.extract()
        return len(self.poems)

    def get_count_total_stanzas(self) -> int:
        if not self.poems:
            self.extract()
        count = 0
        for poem in self.poems:
            count += len(poem.stanzas)
        return count

    def get_count_stanzas_in_poem(self, id: str) -> int:
        poem = self.get_by_id(id)
        length = 0
        for sentences in poem.stanzas:
            length += len(sentences)
        return length

    def get_poems_by_author_id(self, author_id: str) -> List[Poem]:
        if not self.poems:
            self.extract()
        poems = []
        for poem in self.poems:
            if poem.author_id == author_id:
                poems.append(poem)
        return poems
