from collections import UserDict
from collections.abc import Sequence

class MazeData(UserDict):
    def __init__(self, maze_data: dict, size: Sequence[int, int]):
        super().__init__()
        self.data |= dict(maze_data)
        self.size = tuple(size)