from wpimath.controller import PIDController

from autoroutine import AutoRoutine


class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.pid_controller_direc = PIDController(20, 0, 0)
        self.pid_controller_direc.setSetpoint(0)
        self.pid_controller_direc.setTolerance(.05)
        self.pid_controller_dist = PIDController(5 / (2 * goal_in_meters), 0, 0)
        self.pid_controller_dist.setSetpoint(goal_in_meters)
        self.pid_controller_dist.setTolerance(.05)



    def run(self):

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller_direc.calculate(difference)
        distance = self.drivetrain.averageDistanceMeter()
        if self.pid_controller_direc.atSetpoint():
            rotate = 0
        forward = self.pid_controller_dist.calculate(distance)
        if self.pid_controller_dist.atSetpoint():
            self.drivetrain.arcadeDrive(0, 0)
        else:
            print(f"{forward=} {rotate=} {distance=} {difference=}")
            self.drivetrain.arcadeDrive(rotate, forward)
