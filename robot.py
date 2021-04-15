import wpilib
from wpilib import SpeedControllerGroup
import wpilib.drive
from wpilib import XboxController
from wpilib.interfaces import GenericHID
from ctre import WPI_TalonSRX
from networktables import NetworkTables

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        self.leftFront = WPI_TalonSRX(1)
        self.rightFront = WPI_TalonSRX(0)
        self.leftBack = WPI_TalonSRX(2)
        self.rightBack = WPI_TalonSRX(3)

        self.leftDrive = SpeedControllerGroup(self.leftFront, self.leftBack)
        self.rightDrive = SpeedControllerGroup(self.rightFront, self.rightBack)

        self.differentialDrive = wpilib.drive.DifferentialDrive(self.leftDrive, self.rightDrive)

        self.xboxController = XboxController(0)
    
    def teleopPeriodic(self):

        self.differentialDrive.arcadeDrive(-self.xboxController.getY(GenericHID.Hand.kLeftHand),
            self.xboxController.getX(GenericHID.Hand.kRightHand), True)

if __name__ == "__main__":
    wpilib.run(Robot)