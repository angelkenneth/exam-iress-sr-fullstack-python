from app.command.enum import Direction
from app.command.move import MoveCommand
from app.robot.robot import Robot


def test_moving_north():
    robot = Robot(5, 5, 3, 3, Direction.NORTH)
    command = MoveCommand()
    robot = command.invoke(robot)
    assert robot.x_current == 3
    assert robot.y_current == 4
    assert robot.direction == Direction.NORTH


def test_moving_south():
    robot = Robot(5, 5, 3, 3, Direction.SOUTH)
    command = MoveCommand()
    robot = command.invoke(robot)
    assert robot.x_current == 3
    assert robot.y_current == 2
    assert robot.direction == Direction.SOUTH


def test_moving_east():
    robot = Robot(5, 5, 3, 3, Direction.EAST)
    command = MoveCommand()
    robot = command.invoke(robot)
    assert robot.x_current == 4
    assert robot.y_current == 3
    assert robot.direction == Direction.EAST


def test_moving_west():
    robot = Robot(5, 5, 3, 3, Direction.WEST)
    command = MoveCommand()
    robot = command.invoke(robot)
    assert robot.x_current == 2
    assert robot.y_current == 3
    assert robot.direction == Direction.WEST


def test_moving_out_of_bounds(caplog):
    robot = Robot(5, 5, 0, 0, Direction.SOUTH)
    command = MoveCommand()
    robot = command.invoke(robot)
    assert "Moving SOUTH will cause us to fall, aborting" in caplog.messages
    assert robot.x_current == 0
    assert robot.y_current == 0
    assert robot.direction == Direction.SOUTH
