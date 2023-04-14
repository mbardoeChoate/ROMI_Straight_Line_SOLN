# Starter Robot Code
import os

import wpilib
from drivetrain import Drivetrain
from drivestraight import DriveStraight
from wpilib import Joystick, TimedRobot

class Robot(TimedRobot):




    def robotInit(self) -> None:
        self.drivetrain = Drivetrain()
        self.controller=Joystick(0)
        self.drivestraight = DriveStraight(self.drivetrain, .5)

    def robotPeriodic(self) -> None:

        ...

    def teleopInit(self) -> None:
        ...

    def teleopPeriodic(self) -> None:
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(rotate, forward)
        print(f"Forward: {forward}, Rotate: {rotate}")


    def autonomousInit(self) -> None:
        ...

    def autonomousPeriodic(self) -> None:
        self.drivestraight.run()

    def autonomousExit(self) -> None:
        self.drivetrain.resetEncoders()

    def disabledInit(self) -> None:
        pass

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(Robot)