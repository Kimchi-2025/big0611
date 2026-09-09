# game init
from .graphic.render import render_test
from .sound.echo import echo_test

__all__ = ['render_test', 'echo_test']

VERSION = 3.5
print("Initializing game!")


def print_version_info():
    print(f"The version of this game is {VERSION}.")