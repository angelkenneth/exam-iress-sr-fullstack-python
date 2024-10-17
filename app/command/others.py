from typing import TYPE_CHECKING

from app.command.base import BaseCommand
from app.logger import logger

if TYPE_CHECKING:
    from app.robot.robot import Robot


class ReportCommand(BaseCommand):
    def invoke(self, robot: "Robot"):
        logger.info(robot.report)
        return robot


class NoneCommand(BaseCommand):
    def invoke(self, robot: "Robot"):
        """ Do nothing """
        return robot
