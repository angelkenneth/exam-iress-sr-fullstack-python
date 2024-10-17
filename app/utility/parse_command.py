from typing import Tuple


def parse_command_line(command_line: str) -> Tuple[str, Tuple[str]]:
    command_name, *args = list(filter(bool, command_line.split(" ")))
    if args:
        args_1 = ",".join(args)
        command_args = tuple(filter(bool, args_1.split(",")))
        return command_name, command_args
    else:
        return command_name, tuple()
