from typing import List

from app.command.get_from_line import get_command_from_line
from app.logger import logger
from app.robot.robot import Robot
from app.exception.exception import MessagedException


def try_to_run(robot: Robot, command_line: str):
    try:
        command = get_command_from_line(command_line)
    except MessagedException as exception:
        logger.error(exception.message)
        return robot
    return command.invoke(robot)


def run_command_list(robot: Robot, command_list: List[str]):
    for command_item in command_list:
        robot = try_to_run(robot, command_item)
    return robot
