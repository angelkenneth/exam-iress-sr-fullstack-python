from app.command.get_from_line import get_command_from_line
from app.command.place import PlaceCommand
from app.run.from_list import try_to_run
from app.exception.exception import MessagedException
from app.logger import logger
from app.robot.robot import Robot


def try_to_run_1st_command_from_input(robot: Robot):
    command_line = input("Command:")
    try:
        command = get_command_from_line(command_line)
    except MessagedException as exception:
        logger.error(exception.message)
        return try_to_run_1st_command_from_input(robot)
    if isinstance(command, PlaceCommand):
        return command.invoke(robot)
    else:
        logger.warning("First command must be PLACE")
        return try_to_run_1st_command_from_input(robot)


def try_to_run_command_from_input(robot: Robot):
    command_line = input("Command:")
    return try_to_run(robot, command_line)


def intake_commands_from_input():
    logger.info("Welcome to Robo World!")
    robot = Robot(5, 5)
    try:
        robot = try_to_run_1st_command_from_input(robot)
        while True:
            robot = try_to_run_command_from_input(robot)
            if not robot:
                return
    except (KeyboardInterrupt, EOFError):
        logger.info("Thank you for coming!")
        exit(0)
