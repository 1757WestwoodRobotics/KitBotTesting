import wpilib
from wpilib import drive
from ctre import WPI_TalonSRX
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.leftFront = WPI_TalonSRX(5)
        self.rightFront = WPI_TalonSRX(6)
        self.leftBack = WPI_TalonSRX(7)
        self.rightBack = WPI_TalonSRX(8)

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        self.sd.putNumber("Left Front Speed", 0)
        self.sd.putNumber("Right Front Speed", 0)
        self.sd.putNumber("Left Back Speed", 0)
        self.sd.putNumber("Right Back Speed", 0)

        self.sd.putBoolean("Left Run", False)
        self.sd.putBoolean("Right Run", False)

    def teleopPeriodic(self):

        self.leftFrontSpeed = self.sd.getNumber("Left Front Speed", 0)
        self.rightFrontSpeed = self.sd.getNumber("Right Front Speed", 0)
        self.leftBackSpeed = self.sd.getNumber("Left Back Speed", 0)
        self.rightBackSpeed = self.sd.getNumber("Right Back Speed", 0)

        # if self.sd.getBoolean("Left Run", False):
        #     self.leftFrontSpeed = 1
        #     self.leftBackSpeed = 1
            
        # if self.sd.getBoolean("Right Run", False):
        #     self.rightFrontSpeed = 1
        #     self.rightBackSpeed = 1

        self.leftFront.set(self.leftFrontSpeed)
        self.rightFront.set(-self.rightFrontSpeed)
        self.leftBack.set(self.leftBackSpeed)
        self.rightBack.set(-self.rightBackSpeed)

if __name__ == "__main__":
    wpilib.run(Robot)
