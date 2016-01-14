#!/usr/bin/env python3

import wpilib
import networktables
from wpilib.command import Scheduler
from oi import OI

#from subsystems.filename import SubsystemClass

#from commands.filename import CommandClass

from utilities.drive_control import dead_zone

class RobotName(wpilib.SampleRobot):
    def robotInit(self):
        """Initialises robot & joysticks."""

        #self.subsystem = Subsystem(self)

        #self.AutonomousCommand = AutonomousCommand(self)
        self.PlayMacroCommand = PlayMacro(self, "macro.csv")

    def autonomous(self):
        """Autonomous commands go in here."""
        #self.drivetrain.drive.setSafetyEnabled(False) - disable the safety mode on the drivetrain
        self.PlayMacroCommand(self, "macro.csv")

        while self.isAutonomous() and self.isEnabled():
            Scheduler.getInstance().run()
            self.log()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def operatorControl(self):
        """Teleop stuff goes in here"""

        self.PlayMacroCommand.cancel()

        #self.drivetrain.drive.setSafetyEnabled(True) - enables safety things for manual control
        joystick = self.oi.getStick()

        while self.isOperatorControl() and self.isEnabled():
            self.log()
            Scheduler.getInstance().run()
            wpilib.Timer.delay(.005) #don't burn up the cpu

    def disabled(self):
        """When the robot is disabled, this code runs"""

        self.PlayMacroCommand.Cancel()
        while self.isDisabled():
            self.log()
            wpilib.Timer.delay(.005)

    def test(self):
        """Testing things would go here"""
        pass #There's no tests, so just pass

    def log(self):
        """Logging stuff goes here"""
        #self.subsystem.log()

if __name__ == "__main__":
    wpilib.run(RobotName)
