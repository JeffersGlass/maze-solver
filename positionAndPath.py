from dataclasses import dataclass

@dataclass(slots=False)
class PositionAndPrevious():
    position: tuple
    previous: object

    def __repr__(self):
        return f"PositionAndPrevious(position = {self.position}, previous = PositionAndPrevious({self.previous.position}, ...)"