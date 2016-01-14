import wpilib
from wpilib.command import Subsystem
from commands.examplecommand import ExampleCommand

class Subsystem(Subsystem):
    """Example subsystem code"""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.motor = wpilib.Talon(0) #Talons are 0-indexed

    def initDefaultCommand(self):
        self.setDefaultCommand(ExampleCommand())

    def log(self):
        """If there was logging, it would occur here"""
        pass

    def manualSet(self, output):
        self.motor.set(output)
