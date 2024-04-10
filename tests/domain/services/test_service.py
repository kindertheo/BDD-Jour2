from src.domain.services.poem_service import PoemsService
from src.domain.entities.poem import Poem


def test_poem_service_read_all(mocker):
    mocker.patch(
        "src.infrastructure.persistence.file_system.poem_in_file_system.PoemsInFileSystem.extract",
        return_value=[
            Poem(
                id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]]
            )
        ],
    )
    poem_service = PoemsService()
    assert poem_service.read_all()[0].id == "1"


def test_poem_service_read_by_id(mocker):
    mocker.patch(
        "src.infrastructure.persistence.file_system.poem_in_file_system.PoemsInFileSystem.get_by_id",
        return_value=Poem(
            id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]]
        ),
    )
    poem_service = PoemsService()
    assert poem_service.read("id", "1").id == "1"


def test_exception_poem_service_read_by_id(mocker):
    mocker.patch(
        "src.infrastructure.persistence.file_system.poem_in_file_system.PoemsInFileSystem.get_by_id",
        return_value=Poem(
            id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]]
        ),
    )
    poem_service = PoemsService()
    try:
        poem_service.read("id", "3").id == "1"
    except Exception as e:
        assert e == "Poem not found"
