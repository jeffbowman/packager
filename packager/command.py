import os
import logging

logging.basicConfig(level=logging.INFO)

class Command(object):
    """Base class for the commands to run while packaging.

    Provides a default implementation of the `do` method.

    """
    def do(self):
        """do the command.

        Changes to the source directory (if provided) before running the
        command provided in self.execute. Will also make the target directory
        if provided and it doesn't already exist.

        Assumes target directory (if provided) is fully qualified or
        relative to the current directory
        """
        cwd = os.getcwd()

        if self.target != None:
            if not os.path.exists(self.target):
                os.makedirs(self.target)

        if self.source != None:
            os.chdir(self.source)

        logging.info('cmd: ' + self.execute)
        os.system(self.execute)

        os.chdir(cwd)
