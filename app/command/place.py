from copy import copy
from typing import TYPE_CHECKING, Union

from app.command.base import BaseCommand
from app.command.enum import Direction
from app.command.exception import InvalidCommandArgumentException
from app.logger import logger

if TYPE_CHECKING:
    from app.robot.robot import Robot


class PlaceCommand(BaseCommand):
    x_offset: int
    y_offset: int
    direction: Direction

    def __init__(self, x_offset: int, y_offset: int, direction: Direction):
        super().__init__()
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.direction = direction

    @classmethod
    def validate_or_raise(
            cls,
            x_offset: Union[str, int] = None,
            y_offset: Union[str, int] = None,
            direction: Union[str, Direction] = None
    ):
        error_list = []

        try:
            x_offset = int(x_offset)
        except ValueError:
            error_list.append(f"X({x_offset}) must be int")
        try:
            y_offset = int(y_offset)
        except ValueError:
            error_list.append(f"Y({y_offset}) must be int")
        if direction is None:
            error_list.append(f"Argument 3 missing")
        elif not isinstance(direction, Direction):
            try:
                direction = Direction[direction.upper()]
            except KeyError:
                error_list.append(
                    f"Direction must be one of: NORTH,SOUTH,EAST,WEST")

        if error_list:
            raise InvalidCommandArgumentException("; ".join(error_list))

        return PlaceCommand(x_offset, y_offset, direction)

    def invoke(self, robot: "Robot"):
        new_robot = copy(robot)
        new_robot.x_current = self.x_offset
        new_robot.y_current = self.y_offset
        new_robot.direction = self.direction
        if new_robot.is_inbounds:
            return new_robot
        logger.error(f"Coordinates({self.x_offset},{self.y_offset}) are out of bounds, aborting")
        return robot
