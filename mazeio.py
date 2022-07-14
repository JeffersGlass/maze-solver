from collections.abc import Sequence, Collection
from PIL import Image

from mazeData import MazeData
from stores import MazeTypes, MAZE_COLORS
from colorsys import hsv_to_rgb

def load_maze(filename: str):
    """Loads a maze from a given image file, returns a MazeData object"""
    image_data = Image.open(filename)
    size = ((d:= image_data.getbbox())[2], d[3])

    maze_data = dict()

    for x in range(size[0]):
        for y in range(size[1]):
            pixel_data = image_data.getpixel((x, y))
            if sum(pixel_data) > 50*3:
                maze_data[(x, y)] = MazeTypes.EMPTY
            else:
                maze_data[(x, y)] = MazeTypes.WALL

    return MazeData(maze_data, size)

def create_solved_maze_image(maze: MazeData, solve_path: list, hue_speed:float = 0.0001):
    """Given a solved maze and its solution path, creates a PIL image file"""
    img = Image.new("RGB", maze.size, (255,255,255))

    path_length = len(solve_path)

    #Draw maze without path:
    for x in range(maze.size[0]):
        for y in range(maze.size[1]):
            if maze[(x, y)] != MazeTypes.ALREADY_VISITED:
                img.putpixel((x,y), MAZE_COLORS[maze[(x, y)]])
            else:
                img.putpixel((x,y), MAZE_COLORS[MazeTypes.EMPTY])

    #Draw path onto maze. Path color is a rainbow cycle - total number of cycles is equal to hue_speed
    for index, point in enumerate(reversed(solve_path)):
        hue =  (index * hue_speed/path_length) % 1
        raw_color = hsv_to_rgb(hue, 1.0, .5)
        color = tuple([int(c*255) for c in raw_color])

        x, y = point
        img.putpixel((x,y), color)
        
    return img

def display_solved_maze(maze: MazeData, solve_path: list, hue_speed:float = 0.0001):
    """Given a solved maze and its solution path, creates a PIL image file and displays it using the default PNG viewer"""
    img = create_solved_maze_image(maze, solve_path, hue_speed)
    img.show()

def export_solved_maze_image(file_name:str, maze: MazeData, solve_path: list, hue_speed:float = 0.0001):
    """Given a solved maze and its solution path, creates a PIL image file and save it to a file"""
    img = create_solved_maze_image(maze, solve_path, hue_speed)
    img.save(file_name, "PNG")