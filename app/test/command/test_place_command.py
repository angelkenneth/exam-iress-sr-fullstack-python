from pytest import raises

from app.command.enum import Direction
from app.command.exception import InvalidCommandArgumentException
from app.command.get_from_line import PlaceCommand
from app.robot.robot import Robot


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
    with raises(InvalidCommandArgumentException) as exception:
        PlaceCommand.validate_or_raise("1.0", "2", "North")
    assert exception.value.message == "X(1.0) must be int"


def test_invalid_direction():
    with raises(InvalidCommandArgumentException) as exception:
        PlaceCommand.validate_or_raise("1", "2", "Left")
    assert exception.value.message == "Direction must be one of: NORTH,SOUTH,EAST,WEST"


def test_multiple_invalid_argument():
    with raises(InvalidCommandArgumentException) as exception:
        PlaceCommand.validate_or_raise("1.25", "2", "Left")
    assert exception.value.message == "X(1.25) must be int; Direction must be one of: NORTH,SOUTH,EAST,WEST"


def test_no_arguments():
    with raises(InvalidCommandArgumentException) as exception:
        PlaceCommand.validate_or_raise("1", "2")
    assert exception.value.message == "Argument 3 missing"


def test_robot_is_placed_in_the_middle():
    robot = Robot(5, 5)
    command = PlaceCommand(2, 2, Direction.SOUTH)
    robot = command.invoke(robot)
    assert robot.x_current == 2
    assert robot.y_current == 2
    assert robot.direction == Direction.SOUTH


def test_robot_when_robot_is_placed_just_after_boundary(caplog):
    robot = Robot(5, 5)
    command = PlaceCommand(5, 5, Direction.SOUTH)
    robot = command.invoke(robot)
    assert 'Coordinates(5,5) are out of bounds, aborting' in caplog.messages
    assert robot.x_current == 0
    assert robot.y_current == 0
    assert robot.direction == Direction.NORTH


def test_robot_when_robot_is_placed_out_of_bounds(caplog):
    robot = Robot(5, 5)
    command = PlaceCommand(6, 6, Direction.SOUTH)
    robot = command.invoke(robot)
    assert 'Coordinates(6,6) are out of bounds, aborting' in caplog.messages
    assert robot.x_current == 0
    assert robot.y_current == 0
    assert robot.direction == Direction.NORTH


def test_using_negative_coordinates(caplog):
    robot = Robot(5, 5)
    command = PlaceCommand(-1, -1, Direction.SOUTH)
    robot = command.invoke(robot)
    assert 'Coordinates(-1,-1) are out of bounds, aborting' in caplog.messages
    assert robot.x_current == 0
    assert robot.y_current == 0
    assert robot.direction == Direction.NORTH
