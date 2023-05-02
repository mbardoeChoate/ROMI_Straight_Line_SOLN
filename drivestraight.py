import wpilib
from wpimath.controller import PIDController

from autoroutine import AutoRoutine


class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.pid_controller_direc = PIDController(20, 0, 0)
        self.pid_controller_direc.setSetpoint(0)
        self.pid_controller_direc.setTolerance(.005)
        self.pid_controller_dist = PIDController(40 / (7 * goal_in_meters), 0, 0)
        self.pid_controller_dist.setSetpoint(goal_in_meters)
        self.pid_controller_dist.setTolerance(.01)



    def run(self):

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller_direc.calculate(difference)
        distance = self.drivetrain.averageDistanceMeter()
        if self.pid_controller_direc.atSetpoint():
            rotate = 0
        forward = self.pid_controller_dist.calculate(distance)
        forward = max(-.5, min(forward, .5))
        if self.pid_controller_dist.atSetpoint():
            self.drivetrain.arcadeDrive(0, 0)
        else:
            print(f"{forward=:.2f} {rotate=:.2f} {distance=:.2f} {difference=:.4f}")
            self.drivetrain.arcadeDrive(rotate, forward)
        wpilib.SmartDashboard.putNumber("Distance", distance)
