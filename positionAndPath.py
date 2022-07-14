from dataclasses import dataclass

@dataclass(slots=False)
class PositionAndPrevious():
    """
    A utility class to help with path generation.

    Attributes:
        Position (tuple): The (x,y) coordinates of a position in the maze
        Previous (PositionAndPrevious): A pointer to the position before this one in the solve path
    """
    position: tuple
    previous: 'PositionAndPrevious'

    def __repr__(self):
        return f"PositionAndPrevious(position = {self.position}, previous = PositionAndPrevious({self.previous.position}, ...)"