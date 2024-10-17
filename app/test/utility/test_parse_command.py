from app.utility.parse_command import parse_command_line


def test_no_space_args_command():
    command_tuple = parse_command_line("PLACE 1,2,North")
    assert command_tuple == ("PLACE", ("1", "2", "North"))


def test_spaced_args_command():
    command_tuple = parse_command_line("PLACE 1, 2, North")
    assert command_tuple == ("PLACE", ("1", "2", "North"))


def test_wrapped_spaces_command():
    command_tuple = parse_command_line("  PLACE 1, 2, North  ")
    assert command_tuple == ("PLACE", ("1", "2", "North"))


def test_weird_commas():
    command_tuple = parse_command_line("  PLACE 1,, 2, ,, North  ")
    assert command_tuple == ("PLACE", ("1", "2", "North"))
