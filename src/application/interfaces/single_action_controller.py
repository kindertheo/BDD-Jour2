from abc import ABC, abstractmethod


class SingleActionController(ABC):
    @abstractmethod
    def execute(self):
        pass
