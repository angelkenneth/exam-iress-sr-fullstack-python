from app.command.enum import Direction
from app.command.exception import InvalidCommandArgument
from app.command.get_from_line import PlaceCommand
from pytest import raises


def test_valid_arguments():
    command = PlaceCommand.validate_or_raise("1", "2", "North")
    assert command.x_offset == 1
    assert command.y_offset == 2
    assert command.direction == Direction.NORTH


def test_negative_int_str():
    command = PlaceCommand.validate_or_raise("-1", "2", "North")
    assert command.x_offset == -1
    assert command.y_offset == 2
    assert command.direction == Direction.NORTH


def test_direction_enum_str():
    command = PlaceCommand.validate_or_raise("-1", "2", Direction.SOUTH)
    assert command.x_offset == -1
    assert command.y_offset == 2
    assert command.direction == Direction.SOUTH


def test_invalid_decimal_int():
    with raises(InvalidCommandArgument) as exception:
        PlaceCommand.validate_or_raise("1.0", "2", "North")
    assert exception.value.message == "X(1.0) must be int"


def test_invalid_direction():
    with raises(InvalidCommandArgument) as exception:
        PlaceCommand.validate_or_raise("1", "2", "Left")
    assert exception.value.message == "Direction must be one of: NORTH,SOUTH,EAST,WEST"


def test_multiple_invalid_argument():
    with raises(InvalidCommandArgument) as exception:
        PlaceCommand.validate_or_raise("1.25", "2", "Left")
    assert exception.value.message == "X(1.25) must be int; Direction must be one of: NORTH,SOUTH,EAST,WEST"
