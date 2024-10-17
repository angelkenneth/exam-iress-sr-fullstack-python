from app.command.enum import Direction
from app.command.rotate import LeftCommand, RightCommand
from app.robot.robot import Robot


def test_left_from_north_command():
    robot = Robot(5, 5, 0, 0, Direction.NORTH)
    command = LeftCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.WEST


def test_left_from_south_command():
    robot = Robot(5, 5, 0, 0, Direction.SOUTH)
    command = LeftCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.EAST


def test_left_from_east_command():
    robot = Robot(5, 5, 0, 0, Direction.EAST)
    command = LeftCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.NORTH


def test_left_from_west_command():
    robot = Robot(5, 5, 0, 0, Direction.WEST)
    command = LeftCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.SOUTH


def test_right_from_north_command():
    robot = Robot(5, 5, 0, 0, Direction.NORTH)
    command = RightCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.EAST


def test_right_from_south_command():
    robot = Robot(5, 5, 0, 0, Direction.SOUTH)
    command = RightCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.WEST


def test_right_from_east_command():
    robot = Robot(5, 5, 0, 0, Direction.EAST)
    command = RightCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.SOUTH


def test_right_from_west_command():
    robot = Robot(5, 5, 0, 0, Direction.WEST)
    command = RightCommand()
    robot = command.invoke(robot)
    assert robot.direction == Direction.NORTH
