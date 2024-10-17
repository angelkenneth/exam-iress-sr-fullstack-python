import logging

from app.run.from_list import run_command_list
from app.robot.robot import Robot


def test_move_command(caplog):
    """
    Test case from exam
    """
    caplog.set_level(logging.INFO)
    command_list = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    robot = run_command_list(Robot(5, 5), command_list)
    assert robot.report == "0,1,NORTH"
    assert "0,1,NORTH" in caplog.messages


def test_left_command(caplog):
    """
    Test case from exam
    """
    caplog.set_level(logging.INFO)
    command_list = [
        "PLACE 0,0,NORTH",
        "LEFT",
        "REPORT",
    ]
    robot = run_command_list(Robot(5, 5), command_list)
    assert robot.report == "0,0,WEST"
    assert "0,0,WEST" in caplog.messages


def test_all_of_movement(caplog):
    """
    Test case from exam
    """
    caplog.set_level(logging.INFO)
    command_list = [
        "PLACE 1, 2, EAST",
        "MOVE",
        "MOVE",
        "LEFT",
        "MOVE",
        "REPORT",
    ]
    robot = run_command_list(Robot(5, 5), command_list)
    assert robot.report == "3,3,NORTH"
    assert "3,3,NORTH" in caplog.messages
