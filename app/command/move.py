from copy import copy

from app.command.base import BaseCommand
from typing import TYPE_CHECKING

from app.command.enum import Direction
from app.logger import logger

if TYPE_CHECKING:
    from app.robot.robot import Robot


class MoveCommand(BaseCommand):
    def invoke(self, robot: "Robot"):
        new_robot = copy(robot)
        if new_robot.direction == Direction.NORTH:
            new_robot.y_current += 1
        if new_robot.direction == Direction.SOUTH:
            new_robot.y_current -= 1
        if new_robot.direction == Direction.EAST:
            new_robot.x_current += 1
        if new_robot.direction == Direction.WEST:
            new_robot.x_current -= 1
        if new_robot.is_inbounds:
            return new_robot
        logger.error(
            f"Moving {robot.direction.name} will cause us to fall, aborting")
        return robot
