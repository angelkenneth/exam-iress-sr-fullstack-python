def test_move_command():
    command_list = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    expected = "0,1,NORTH"
    assert False


def test_left_command():
    command_list = [
        "PLACE 0,0,NORTH",
        "MOVE",
        "REPORT",
    ]
    expected = "0,0,WEST"
    assert False


def test_all_of_movement():
    command_list = [
        "PLACE 1, 2, EAST",
        "MOVE",
        "MOVE",
        "LEFT",
        "MOVE",
        "REPORT",
    ]
    expected = "3,3,NORTH"
    assert False


"""
TODO Other cases:
1. Assure does not fall off the edge
"""
