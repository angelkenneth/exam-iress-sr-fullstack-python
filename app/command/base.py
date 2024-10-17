from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.robot.robot import Robot


class BaseCommand:
    def __init__(self, *args):
        pass

    @classmethod
    def validate_or_raise(cls, *args):
        return cls(*args)

    def invoke(self, robot: "Robot"):
        raise NotImplementedError()
