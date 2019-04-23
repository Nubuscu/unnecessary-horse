import os
from .command import Command

class OpenFileCommand(Command):
    def __init__(self, _filepath):
        self._filepath = _filepath

    def execute(self, params):
        os.startfile(self._filepath)

    def names(self):
        """ Command is identified by the name of the shortcut it represents.
        There are no aliases at present.
        """
        _file = self._filepath.split(os.sep)[-1]
        _filename = _file.split('.')[0]
        return [_filename]
