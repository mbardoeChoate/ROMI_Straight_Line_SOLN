from autoroutine import AutoRoutine
from wpimath.controller import PIDController


class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.pid_controller=PIDController(20, 0, 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)

        #self.kp = -20

    def run(self):

        difference = self.drivetrain.getLeftDistanceMeter() - self.drivetrain.getRightDistanceMeter()
        rotate=self.pid_controller.calculate(difference)
        if self.pid_controller.atSetpoint():
            rotate=0
        if self.drivetrain.averageDistanceMeter() > self.goal:
            self.drivetrain.arcadeDrive(0, 0)
        else:
            #rotate = difference * self.kp
            # rotate=0
            forward = .4
            print(
                f"Fwd: {forward}, Rot: {rotate}  distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")
            self.drivetrain.arcadeDrive(rotate, forward)
