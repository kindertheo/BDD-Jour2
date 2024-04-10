from src.application.interfaces.single_action_controller import SingleActionController
from src.domain.services.poet_service import PoetsService

class FindPoetByIdController(SingleActionController):
    def __init__(self, id):
        self.poet_service = PoetsService()
        self.id = id

    def execute(self):
        return self.poet_service.read(key="id", value=self.id)

class FindPoetByFirstnameController(SingleActionController):
    def __init__(self, firstname):
        self.poet_service = PoetsService()
        self.firstname = firstname

    def execute(self):
        return self.poet_service.read(key="firstname", value=self.firstname)

class FindPoetByLastnameController(SingleActionController):
    def __init__(self, lastname):
        self.poet_service = PoetsService()
        self.lastname = lastname

    def execute(self):
        return self.poet_service.read(key="lastname", value=self.lastname)

class CountPoetsController(SingleActionController):
    def __init__(self):
        self.poet_service = PoetsService()

    def execute(self):
        return self.poet_service.count_authors()
