from wpimath.controller import PIDController

from autoroutine import AutoRoutine
from drivetrain import Drivetrain


class ClimbRamp(AutoRoutine):

    def __init__(self, drivetrain: Drivetrain):
        self.drivetrain = drivetrain
        self.drivetrain.resetGyro()
        # self.started_ramp = False
        # self.ended_ramp = False
        self.pid_controller = PIDController(4 / 10000, 2 / 10000, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(10)
        self.drivetrain.resetEncoders()
        # self.forward_rate = .8
        self.reset()

    def run(self):
        if not (self.started_ramp or self.ended_ramp):
            self.drive_straight()
            tip = self.drivetrain.getGyroAngleY()
            print(f"{tip=}")
            if tip > 7:
                print("On Ramp")
                self.forward_rate = .5
                self.started_ramp = True
        elif self.started_ramp and not self.ended_ramp:
            self.drive_straight()
            tip = self.drivetrain.getGyroAngleY()
            print(f"{tip=}")
            if tip < 4:
                print("Finished Ramp")
                self.forward_rate = 0
                self.ended_ramp = True
        else:
            self.drivetrain.arcadeDrive(0, 0)

    def drive_straight(self):
        #
        error = self.drivetrain.getLeftEncoderCount() - self.drivetrain.getRightEncoderCount()
        power = self.pid_controller.calculate(error)
        at_set_point = self.pid_controller.atSetpoint()

        print(f"{at_set_point=} {power} {error=}")
        if not at_set_point:
            self.drivetrain.arcadeDrive(power, self.forward_rate)
        else:
            self.drivetrain.arcadeDrive(0, self.forward_rate)

    def reset(self) -> None:
        self.ended_ramp = False
        self.started_ramp = False
        self.forward_rate = .8
