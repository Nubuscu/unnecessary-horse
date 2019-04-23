import webbrowser
from .command import Command

class WebSearchCommand(Command):

    def execute(self, params):
        webbrowser.open_new_tab('https://www.google.com/search?q=' + " ".join(params))

    def names(self):
        return {'search', 'google'}