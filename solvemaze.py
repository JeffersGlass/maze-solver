from collections import deque
from collections.abc import Sequence
import json
import pickle

from stores import MazeTypes
from positionAndPath import PositionAndPrevious



def solve_maze(maze: dict) -> dict:
    stack = deque()

    start = maze.start
    end = maze.end

    stack.append(PositionAndPrevious(start, None))    

    #We'll print the size of the stack every step, to track our progress some
    stack_print_counter = 0
    STACK_PRINT_EVERY = 50000

    #We'll pause and display the image every so often
    SHOW_IMAGE_EVERY = 50_000

    while len(stack) > 0:
        #We'll print the size of the stack every step, to track our progress some
        stack_print_counter +=1
        if not stack_print_counter % STACK_PRINT_EVERY: print(f"{stack_print_counter: <6}: Stack length: {len(stack)}")
        #if not stack_print_counter % SHOW_IMAGE_EVERY: display_all_searched_maze(maze)

        current_position_and_previous = stack.pop()
        current_position = current_position_and_previous.position

        if maze[current_position] == MazeTypes.END:
            print("END FOUND!")
            path = find_path(maze, current_position_and_previous)
            return maze, path
        if maze[current_position] == MazeTypes.ALREADY_VISITED:
            continue
        
        maze[current_position] = MazeTypes.ALREADY_VISITED

        for delta in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            check_position = (current_position[0] + delta[0], current_position[1] + delta[1])
            if is_valid_position(check_position, maze.size):
                if  maze[check_position] in  [MazeTypes.EMPTY, MazeTypes.END]:
                    new_position = PositionAndPrevious(check_position, current_position_and_previous)
                    #print(f"Adding {new_position} to stack")
                    stack.append(new_position)

    print("COULD NOT FIND SOLUTION")
    return maze

def is_valid_position(pos: Sequence[int, int], size:Sequence[int, int]) -> bool:
    return (pos[0] >= 0 and \
            pos[1] >= 0 and \
            pos[0] < size[0] and \
            pos[1] < size[1]
            )

def find_path(maze, position_and_previous):
    path = [position_and_previous.position]
    search_position = position_and_previous
    while search_position.previous is not None:
        search_position = search_position.previous
        path.append(search_position.position)

    print(f"Path Determined (length {len(path)})")
    return path

def export_path(path, filepath):
    with open(filepath, mode='w', encoding='UTF-8') as outfile:
        json.dump(path, outfile)

def import_path(filepath):
    with open(filepath, mode='r', encoding='UTF-8') as infile:
        return json.load(infile)

def export_maze(maze, filepath):
    with open(filepath, mode='wb') as outfile:
        pickle.dump(maze, outfile, pickle.HIGHEST_PROTOCOL)

def import_maze(filepath):
    with open(filepath, mode='rb') as infile:
        return pickle.load(infile)