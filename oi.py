import wpilib
from networktables import NetworkTable
from wpilib.buttons import JoystickButton, InternalButton
from utilities.pov_button import POVButton

#from commands.command_filename import CommandClass

class OI:
    """Button mapping goes here"""
    def __init__(self, robot):
        self.stick = wpilib.Joystick(0)
        self.smart_dashboard = NetworkTable.getTable("SmartDashboard")

        #button_number = JoystickButton(self.stick, 1)
        #button_number.whenPressed(Command(robot))
        #button_number.whileHeld(Command(robot))

    def getStick(self):
        return self.stick
