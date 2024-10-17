from copy import copy
from typing import TYPE_CHECKING

from app.command.base import BaseCommand
from app.command.enum import Direction

if TYPE_CHECKING:
    from app.robot.robot import Robot


class LeftCommand(BaseCommand):
    def invoke(self, robot: "Robot"):
        new_robot = copy(robot)
        if new_robot.direction == Direction.NORTH:
            new_robot.direction = Direction.WEST
        elif new_robot.direction == Direction.SOUTH:
            new_robot.direction = Direction.EAST
        elif new_robot.direction == Direction.EAST:
            new_robot.direction = Direction.NORTH
        elif new_robot.direction == Direction.WEST:
            new_robot.direction = Direction.SOUTH
        return new_robot


class RightCommand(BaseCommand):
    def invoke(self, robot: "Robot"):
        new_robot = copy(robot)
        if new_robot.direction == Direction.NORTH:
            new_robot.direction = Direction.EAST
        elif new_robot.direction == Direction.SOUTH:
            new_robot.direction = Direction.WEST
        elif new_robot.direction == Direction.EAST:
            new_robot.direction = Direction.SOUTH
        elif new_robot.direction == Direction.WEST:
            new_robot.direction = Direction.NORTH
        return new_robot

