from wpilib.command import command

class ExampleCommand(Command):
    """Example command class"""
    def __init__(self, robot):
        super().__init__()
        self.robot
        self.requires(self.robot.subsystem)

    def execute(self):
        """Execution code goes here"""
        pass

    def isFinished(self):
        return False

    def cancel(self):
        super().cancel()
