from app.command.exception import UnknownCommandException
from app.command.move import MoveCommand
from app.command.others import ReportCommand, NoneCommand
from app.command.place import PlaceCommand
from app.command.rotate import RightCommand, LeftCommand
from app.utility.parse_command import parse_command_line


def get_command_from_line(command_str: str):
    command, args = parse_command_line(command_str)
    command = command.upper()
    if command == "PLACE":
        return PlaceCommand.validate_or_raise(*args)
    if command == "MOVE":
        return MoveCommand.validate_or_raise()
    if command == "LEFT":
        return LeftCommand.validate_or_raise()
    if command == "RIGHT":
        return RightCommand.validate_or_raise()
    if command == "REPORT":
        return ReportCommand.validate_or_raise()
    if command == "NONE":
        return NoneCommand.validate_or_raise()
    raise UnknownCommandException(command)
