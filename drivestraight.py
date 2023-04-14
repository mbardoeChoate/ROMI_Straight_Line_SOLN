
class DriveStraight:

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain=drivetrain
        self.goal=goal_in_meters
        self.kp=-20

    def run(self):

        difference=self.drivetrain.getLeftDistanceMeter()-self.drivetrain.getRightDistanceMeter()
        if self.drivetrain.averageDistanceMeter() > self.goal:
            self.drivetrain.arcadeDrive(0,0)
        else:
            #rotate=difference*self.kp
            rotate=0
            forward=.4
            print(f"Fwd: {forward}, Rot: {rotate}  distance:{self.drivetrain.averageDistanceMeter()} difference:{difference}")
            self.drivetrain.arcadeDrive(rotate, forward)