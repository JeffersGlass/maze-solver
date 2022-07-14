from collections import UserDict
from collections.abc import Sequence

class MazeData(UserDict):
    """
    A utility class for holding the data associated with a Maze

    Attributes:
        data (dict): The pixel-by-pixel information about the maze. Accessible via subscripting[]. 0-indexed.
        size (tuple): The size of the maze, in (x, y) format.
    """
    def __init__(self, maze_data: dict, size: Sequence[int, int]):
        super().__init__()
        self.data |= dict(maze_data)
        self.size = tuple(size)