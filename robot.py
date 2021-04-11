import wpilib
from wpilib import drive
from ctre import WPI_TalonSRX
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.leftFront = WPI_TalonSRX(0)
        self.rightFront = WPI_TalonSRX(1)
        self.leftBack = WPI_TalonSRX(2)
        self.rightBack = WPI_TalonSRX(3)

        NetworkTables.initialize(server="10.17.57.2")
        self.sd = NetworkTables.getTable("SmartDashboard")

        self.sd.putNumber("Talon", self.leftFront.getDeviceID(), "Speed", 0)
        self.sd.putNumber("Talon", self.leftBack.getDeviceID(), "Speed", 0)
        self.sd.putNumber("Talon", self.rightFront.getDeviceID(), "Speed", 0)
        self.sd.putNumber("Talon", self.rightBack.getDeviceID(), "Speed", 0)

    def teleopPeriodic(self):

        self.leftFrontSpeed = self.sd.getNumber("Talon", self.leftFront.getDeviceID(), "Speed", 0)
        self.rightFrontSpeed = self.sd.getNumber("Talon", self.rightFront.getDeviceID(), "Speed", 0)
        self.leftBackSpeed = self.sd.getNumber("Talon", self.leftBack.getDeviceID(), "Speed", 0)
        self.rightBackSpeed = self.sd.getNumber("Talon", self.rightBack.getDeviceID(), "Speed", 0)

        self.leftFront.set(self.leftFrontSpeed)
        self.rightFront.set(-self.rightFrontSpeed)
        self.leftBack.set(self.leftBackSpeed)
        self.rightBack.set(-self.rightBackSpeed)

if __name__ == "__main__":
    wpilib.run(Robot)