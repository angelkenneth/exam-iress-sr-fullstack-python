from app.command.enum import Direction
from app.robot.robot import Robot


def test_report():
    robot = Robot(5, 5)
    assert robot.report == f"0,0,{Direction.NORTH.name}"


def test_is_inbounds():
    robot = Robot(5, 5, 5, 5)
    assert not robot.is_inbounds
    assert robot.is_out_of_bounds


def test_is_out_of_bounds():
    robot = Robot(5, 5, 1, 1)
    assert robot.is_inbounds
    assert not robot.is_out_of_bounds
