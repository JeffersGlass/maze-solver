from collections import deque
from collections.abc import Sequence
import json
import pickle
from mazeData import MazeData

from stores import MazeTypes
from positionAndPath import PositionAndPrevious

def solve_maze(maze: dict, start: Sequence[int, int], end:Sequence[int, int]) -> tuple[MazeData, list]:
    """Given a loaded maze file, find the path between start and end"""

    #Use a stack for O(1) pop() and append() operations
    stack = deque()

    maze[end] = MazeTypes.END

    stack.append(PositionAndPrevious(start, None))    

    #We'll print the size of the stack every so often, to track our progress some
    stack_print_counter = 0
    STACK_PRINT_EVERY = 50000

    while len(stack) > 0:
        #We'll print the size of the stack every so often, to track our progress some
        stack_print_counter +=1
        if not stack_print_counter % STACK_PRINT_EVERY: print(f"{stack_print_counter: <6}: Stack length: {len(stack)}")

        current_position_and_previous = stack.pop()
        current_position = current_position_and_previous.position

        if maze[current_position] == MazeTypes.END:
            print("END FOUND!")
            path = flatten_path(current_position_and_previous)
            return maze, path
        if maze[current_position] == MazeTypes.ALREADY_VISITED: #No need to check a coordinate twice
            continue
        
        maze[current_position] = MazeTypes.ALREADY_VISITED

        #Check the 4 neighboring locations, and add them to the stack if they're not out-of-bounds
        for delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            check_position = (current_position[0] + delta[0], current_position[1] + delta[1])
            if is_valid_position(check_position, maze.size):
                if  maze[check_position] in  [MazeTypes.EMPTY, MazeTypes.END]:
                    new_position = PositionAndPrevious(check_position, current_position_and_previous)
                    stack.append(new_position)

    print("COULD NOT FIND SOLUTION")
    return maze, None

def is_valid_position(pos: Sequence[int, int], size:Sequence[int, int]) -> bool:
    """Determines if the given coordinates are within a maze of the given size"""
    return (pos[0] >= 0 and \
            pos[1] >= 0 and \
            pos[0] < size[0] and \
            pos[1] < size[1]
            )

def flatten_path(position_and_previous):
    """Given a linked-list style path from the solving process, return a flat list of the solve path"""
    path = [position_and_previous.position]
    search_position = position_and_previous
    while search_position.previous is not None:
        search_position = search_position.previous
        path.append(search_position.position)

    print(f"Path Determined (length {len(path)})")
    return path

def export_path(path, filepath):
    """Export a flattened path to a json file"""
    with open(filepath, mode='w', encoding='UTF-8') as outfile:
        json.dump(path, outfile)

def import_path(filepath):
    """Import a flattened path from a json file"""
    with open(filepath, mode='r', encoding='UTF-8') as infile:
        return json.load(infile)

def export_maze(maze, filepath):
    """Export a maze (solved or unsolved) via pickling"""
    with open(filepath, mode='wb') as outfile:
        pickle.dump(maze, outfile, pickle.HIGHEST_PROTOCOL)

def import_maze(filepath):
    """Import a maze (solved or unsolved) via pickling"""
    with open(filepath, mode='rb') as infile:
        return pickle.load(infile)