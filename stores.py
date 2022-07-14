from enum import Enum, auto

class MazeTypes(Enum):
    """
    States a particular coordinate in a maze can be; changed when the maze is solved
    """
    EMPTY = auto()
    WALL = auto()
    ALREADY_VISITED = auto()
    END = auto()

MAZE_COLORS = {
    MazeTypes.EMPTY: (255,255,255),
    MazeTypes.WALL: (0,0,0),
    MazeTypes.ALREADY_VISITED: (0,255,0),
    MazeTypes.END: (255,0,255),
}