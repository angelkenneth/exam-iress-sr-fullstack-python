from app.command.base import BaseCommand
from app.command.enum import Direction
from app.command.exception import InvalidCommandArgument


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
            x_offset: str | int,
            y_offset: str | int,
            direction: str | Direction
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
        if not isinstance(direction, Direction):
            try:
                direction = Direction[direction.upper()]
            except KeyError:
                error_list.append(
                    f"Direction must be one of: NORTH,SOUTH,EAST,WEST")

        if error_list:
            raise InvalidCommandArgument("; ".join(error_list))

        return PlaceCommand(x_offset, y_offset, direction)
