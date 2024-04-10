from src.infrastructure.persistence.file_system.poem_in_file_system import (
    PoemsInFileSystem,
)
from src.domain.entities.poem import Poem


def test_poems_list_json(mocker):
    mocker.patch("os.listdir", return_value=["file1.json", "file2.json"])
    poems_in_file_system = PoemsInFileSystem()
    assert poems_in_file_system.list_json() == ["file1.json", "file2.json"]


def test_poems_read_json(mocker):
    mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data="data"),
    )
    poems_in_file_system = PoemsInFileSystem()
    assert poems_in_file_system.read_json("file1.json") == "data"


def test_convert_to_class():
    data = """{
        "id": "1",
        "title": "title",
        "author_id": "1",
        "stanzas": [["stanza1"], ["stanza2"]] 
        }
        """

    poems_in_file_system = PoemsInFileSystem()
    assert poems_in_file_system.convert_to_class(data).id == "1"
    assert poems_in_file_system.convert_to_class(data).title == "title"
    assert poems_in_file_system.convert_to_class(data).author_id == "1"
    assert poems_in_file_system.convert_to_class(data).stanzas == [
        ["stanza1"],
        ["stanza2"],
    ]


def test_get_by_id():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    poem = poems_in_file_system.get_by_id("1")
    assert isinstance(poem, Poem)

def test_get_by_id_exception():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    try:
        poems_in_file_system.get_by_id("2")
    except Exception as e:
        assert str(e) == "Poem not found"

def test_get_by_title():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    poem = poems_in_file_system.get_by_title("title")
    assert isinstance(poem, Poem)

def test_get_by_title_exception():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    try:
        poems_in_file_system.get_by_title("title2")
    except Exception as e:
        assert str(e) == "Poem not found"

def test_get_by_author_id():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    poems = poems_in_file_system.get_by_author_id("1")
    assert isinstance(poems[0], Poem)

def test_get_by_author_id_exception():
    poems_in_file_system = PoemsInFileSystem()
    poems_in_file_system.poems = [
        Poem(id="1", title="title", author_id="1", stanzas=[["stanza1"], ["stanza2"]])
    ]
    try:
        poems_in_file_system.get_by_author_id("2")
    except Exception as e:
        assert str(e) == "Poems not found"
