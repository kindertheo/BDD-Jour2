from src.application.interfaces.single_action_controller import SingleActionController
from src.domain.services.poem_service import PoemsService


class FindPoemByAuthorIdController(SingleActionController):
    def __init__(self, author_id):
        self.poem_service = PoemsService()
        self.author_id = author_id

    def execute(self):
        return self.poem_service.read(key="author_id", value=self.author_id)


class FindPoemByIdController(SingleActionController):
    def __init__(self, author_id):
        self.poem_service = PoemsService()
        self.author_id = author_id

    def execute(self):
        return self.poem_service.read(key="id", value=self.author_id)


class FindPoemByTitleController(SingleActionController):
    def __init__(self, title):
        self.poem_service = PoemsService()
        self.title = title

    def execute(self):
        return self.poem_service.read(key="title", value=self.title)


class CountPoemStanzasByIdController(SingleActionController):
    def __init__(self, id):
        self.poem_service = PoemsService()
        self.id = id

    def execute(self):
        return self.poem_service.count_poems_stanzas_by_id(self.id)


class CountPoemsController(SingleActionController):
    def __init__(self):
        self.poem_service = PoemsService()

    def execute(self):
        return self.poem_service.count_poems()

