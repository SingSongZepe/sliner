import typing

from enum import Enum

class Mode(Enum):
    Emp = 0     # just mouse
    Point = 1
    Line = 2    # create a line
    Arc = 3     # create a arc
    Trim = 4    # trim line
    Delete = 5  # delete

    def eq(mode1: 'Mode', mode2: 'Mode') -> bool:
        return mode1 == mode2
    
    def string(mode: 'Mode') -> str:
        if mode == Mode.Emp:
            return 'Emp'
        elif mode == Mode.Point:
            return 'Point'
        elif mode == Mode.Line:
            return 'Line'
        elif mode == Mode.Arc:
            return 'Arc'
        elif mode == Mode.Trim:
            return 'Trim'
        elif mode == Mode.Delete:
            return 'Delete'
        raise TypeError('Unknown kind of mode')