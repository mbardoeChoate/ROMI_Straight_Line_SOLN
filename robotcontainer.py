import wpilib

from autoroutine import AutoRoutine
from drivestraight import DriveStraight
from drivetrain import Drivetrain
from gyroturn import GyroTurn


class RobotContainer:

    def __init__(self) -> None:
        self.controller = wpilib.Joystick(0)
        # Create SmartDashboard chooser for autonomous routines
        self.chooser = wpilib.SendableChooser()
        self.drivetrain = Drivetrain()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Twist 90 degrees", GyroTurn(self.drivetrain, 90))
        self.chooser.addOption("Go straight 2m", DriveStraight(self.drivetrain, 2))
        wpilib.SmartDashboard.putData(self.chooser)

    def get_autonomous(self) -> AutoRoutine:
        return self.chooser.getSelected()
