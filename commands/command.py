class Command:
    def execute(self, params):
        """Method that runs the command. 
        This will vary depending on the implementation but likely opens another application, displays information, etc.
        The implementation should always gracefully dispose after running.
        e.g. if information is displayed, wait for input to exit. if another app is opened, detach the thread and exit.
        """
        raise NotImplementedError

    def names(self):
        """
        Return a list of string names that this command should respond to.
        e.g. ['browser', 'browse', 'b', 'chrome']
        """
        raise NotImplementedError