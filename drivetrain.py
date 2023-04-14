
import wpilib
from wpilib.drive import DifferentialDrive
import math
from wpilib import Spark
class Drivetrain:


    def __init__(self):
        self.kCountsPerRevolution = 1440.0
        self.kWheelDiameterMeter = 0.07
        self.left_motor=Spark(0)
        self.right_motor=Spark(1)
        self.leftEncoder = wpilib.Encoder(4, 5)
        self.rightEncoder = wpilib.Encoder(6, 7)
        # Set up the differential drive controller
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        # Use meters as unit for encoder distances
        self.leftEncoder.setDistancePerPulse(
            (math.pi * self.kWheelDiameterMeter) / self.kCountsPerRevolution
        )
        self.rightEncoder.setDistancePerPulse(
            (math.pi * self.kWheelDiameterMeter) / self.kCountsPerRevolution
        )
        self.resetEncoders()

    def resetEncoders(self) -> None:
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
        self.rightEncoder.reset()

    def getLeftEncoderCount(self) -> int:
        return self.leftEncoder.get()

    def getRightEncoderCount(self) -> int:
        return self.rightEncoder.get()

    def getLeftDistanceMeter(self) -> float:
        return self.leftEncoder.getDistance()

    def getRightDistanceMeter(self) -> float:
        return self.rightEncoder.getDistance()
