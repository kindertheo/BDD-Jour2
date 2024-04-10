import sys
from .domain.entities.poem import Poem
from src.application.adapters.console.actions.poem_controller import (
    FindPoemByAuthorIdController,
    FindPoemByIdController,
    FindPoemByTitleController,
)

from src.application.adapters.console.actions.poet_controller import (
    FindPoetByIdController,
    FindPoetByFirstnameController,
    FindPoetByLastnameController,
)

class App:
    def run(self):
        print("App is running")
        try:
            action = sys.argv[1]
            argument_name = sys.argv[2]
            argument_value = sys.argv[3]
            command = f"{action}_{argument_name}"
        except IndexError:
            print("Invalid arguments")
            return

        controllers = {
            "read_author_id": FindPoemByAuthorIdController,
            "read_id": FindPoemByIdController,
            "read_title": FindPoemByTitleController,
            "read_poet_id": FindPoetByIdController,
            "read_poet_firstname": FindPoetByFirstnameController,
            "read_poet_lastname": FindPoetByLastnameController,
        }

        if command in controllers:
            result = controllers[command](argument_value).execute()
            print(result)
            return result
        else:
            print("Invalid command")
            return
