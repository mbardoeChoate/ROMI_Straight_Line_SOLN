from drivetrain import Drivetrain


class GyroTurn:

    def __init__(self, drivetrain: Drivetrain, angle: float):
        self.angle = angle
        self.drivetrain = drivetrain
        self.kp = 1 / 25
        self.ki = 1 / 800
        self.drivetrain.resetGyro()
        self.total_error = 0

    def run(self):
        current_reading = self.drivetrain.getGyroAngleZ()
        error = self.angle - current_reading
        self.total_error += error
        self.total_error = min(500, self.total_error)
        # print(f"gyro: {current_reading} push: {self.kp * error}")
        if abs(error) > 1:
            power = min(.4, max(-.4, self.kp * error + self.ki * self.total_error))
            print(f"gyro: {current_reading} push: {power}")
            self.drivetrain.arcadeDrive(power, 0)
        else:
            self.drivetrain.arcadeDrive(0, 0)
            self.total_error = 0
