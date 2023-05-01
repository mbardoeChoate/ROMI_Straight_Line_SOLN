from drivetrain import Drivetrain
from wpimath.controller import PIDController
from autoroutine import AutoRoutine


class GyroTurn(AutoRoutine):
    def __init__(self, drivetrain: Drivetrain, angle: float):
        self.angle = angle
        self.drivetrain = drivetrain
        self.pid_controller = PIDController(1 / 60, 1 / 20, 1 / 650)
        self.pid_controller.setIntegratorRange(-0.1, 0.1)
        self.pid_controller.setSetpoint(self.angle)
        self.pid_controller.setTolerance(1)
        # self.kp = 1 / 25
        # self.ki = 1 / 800
        self.drivetrain.resetGyro()
        # self.total_error = 0

    def run(self):
        current_reading = self.drivetrain.getGyroAngleZ()
        power = self.pid_controller.calculate(current_reading)
        atSetpoint = self.pid_controller.atSetpoint()
        position_error = self.pid_controller.getPositionError()
        velocity_error = self.pid_controller.getVelocityError()
        print(
            f"{current_reading=:.2f}  {power=:.2f} {atSetpoint=} {position_error=:.2f} {velocity_error=:.2f}"
        )
        if not atSetpoint:
            self.drivetrain.arcadeDrive(power, 0)
        else:
            self.drivetrain.arcadeDrive(0, 0)

        # error = self.angle - current_reading
        # self.total_error += error
        # self.total_error = min(500, self.total_error)
        # # print(f"gyro: {current_reading} push: {self.kp * error}")
        # if abs(error) > 1:
        #     power = min(.4, max(-.4, self.kp * error + self.ki * self.total_error))
        #     print(f"gyro: {current_reading} push: {power}")
        #     self.drivetrain.arcadeDrive(power, 0)
        # else:
        #     self.drivetrain.arcadeDrive(0, 0)
        #     self.total_error = 0
