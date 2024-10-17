from app.command.exception import UnknownCommandException
from app.command.get_from_line import get_command_from_line
from app.command.others import LeftCommand
from app.command.place import PlaceCommand
from pytest import raises


def test_place_command():
    command = get_command_from_line("PLACE 0,0,North")
    assert isinstance(command, PlaceCommand)


def test_casing_command():
    command = get_command_from_line("Left")
    assert isinstance(command, LeftCommand)


def test_invalid_command():
    with raises(UnknownCommandException):
        get_command_from_line("INVALID")
