import json
import os
from .web_search import WebSearchCommand
from .open_file import OpenFileCommand

_settings = json.loads(open('settings.json', 'r').read())
_shortcuts = []
for r, d, f in os.walk(_settings['directory']):
    for _file in f:
        _shortcuts.append(os.path.join(r, _file))
available = {
    WebSearchCommand()
    # other commands here
    }.union({
        OpenFileCommand(f) for f in _shortcuts
    })