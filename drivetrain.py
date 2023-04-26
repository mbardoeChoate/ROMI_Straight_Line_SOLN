
import wpilib
from wpilib.drive import DifferentialDrive
import math
from wpilib import Spark, Encoder
import romi
class Drivetrain:


    def __init__(self):
        self.kCountsPerRevolution = 1440.0
        self.kWheelDiameterMeter = 0.07
        self.left_motor=Spark(0)
        self.right_motor=Spark(1)
        self.leftEncoder = Encoder(4, 5)
        self.rightEncoder = Encoder(6, 7)
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

        # Set up the RomiGyro
        self.gyro = romi.RomiGyro()

        # Set up the BuiltInAccelerometer
        self.accelerometer = wpilib.BuiltInAccelerometer()

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

    def averageDistanceMeter(self) -> float:
        return (self.getRightDistanceMeter()+self.getLeftDistanceMeter())/2.0

    def arcadeDrive(self, rot: float, fwd: float, ) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        self.drive.arcadeDrive(rot, fwd)

    def getAccelX(self) -> float:
        """The acceleration in the X-axis.

        :returns: The acceleration of the Romi along the X-axis in Gs
        """
        return self.accelerometer.getX()

    def getAccelY(self) -> float:
        """The acceleration in the Y-axis.

        :returns: The acceleration of the Romi along the Y-axis in Gs
        """
        return self.accelerometer.getY()

    def getAccelZ(self) -> float:
        """The acceleration in the Z-axis.

        :returns: The acceleration of the Romi along the Z-axis in Gs
        """
        return self.accelerometer.getZ()

    def getGyroAngleX(self) -> float:
        """Current angle of the Romi around the X-axis.

        :returns: The current angle of the Romi in degrees
        """
        return self.gyro.getAngleX()

    def getGyroAngleY(self) -> float:
        """Current angle of the Romi around the Y-axis.

        :returns: The current angle of the Romi in degrees
        """
        return self.gyro.getAngleY()

    def getGyroAngleZ(self) -> float:
        """Current angle of the Romi around the Z-axis.

        :returns: The current angle of the Romi in degrees
        """
        return self.gyro.getAngleZ()

    def resetGyro(self) -> None:
        """Reset the gyro"""
        self.gyro.reset()