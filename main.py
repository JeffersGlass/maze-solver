from mazeio import load_maze, display_solved_maze
from solvemaze import export_maze, export_path, solve_maze, import_maze, import_path

def main():
    #The filename and extension for the maze file
    maze_name = 'hardestmaze'
    extension = 'jpg'

    #Where to start and end the solve
    start = (0,0)
    end = (1000, 1000)

    #File locations for caching solutions
    maze_file = f'{maze_name}_{start[0]}-{start[1]}_{end[0]}-{end[1]}_solved.pickle'
    path_file = f'{maze_name}_{start[0]}-{start[1]}_{end[0]}-{end[1]}_path_solved.json'


    try: # Used catched maze solution if it exists
        result = import_maze(maze_file)
        path = [tuple(t) for t in import_path(path_file)]
    except FileNotFoundError as err:
        print(err)
        print("Solution or path not found, solving maze fresh")

        my_maze = load_maze(f'{maze_name}.{extension}')
        result, path = solve_maze(my_maze, start, end)

        # Save solution for next time to speed up printing
        export_maze(result, maze_file)
        export_path(path, path_file)
    else:
        print("Solution and path found, using solution from file")

    display_solved_maze(result, path, hue_speed = 2)

if __name__ == '__main__':
    main()
