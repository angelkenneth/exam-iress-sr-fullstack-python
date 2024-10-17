from app.command.run_from_list import try_to_run
from app.logger import logger
from app.robot.robot import Robot


def try_to_run_command_from_input(robot: Robot):
    command_line = input("Command:")
    return try_to_run(robot, command_line)


def intake_commands_from_input():
    logger.info("Welcome to Robo World!")
    robot = Robot(5, 5)
    try:
        while True:
            robot = try_to_run_command_from_input(robot)
            if not robot:
                return
    except (KeyboardInterrupt, EOFError):
        logger.info("Thank you for coming!")
        exit(0)
