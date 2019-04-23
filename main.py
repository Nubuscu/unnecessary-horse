import sys
import os
import json
from commands import available as avl_commands

def process_args():
    # TODO allow to be invoked as one-liner e.g. launcho google puppies
    args = input("Enter a command: ").split(" ")
    return args[0], args[1:]

if __name__ == "__main__":
    name, params = process_args()
    for command in avl_commands:
        if name in command.names():
            command.execute(params)