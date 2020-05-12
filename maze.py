import numpy as np
import queue


def read_maze(src):
    # Function to read the txt file and convert it to a numpy 2D array
    f = open(src, 'r')
    x = []
    for line in f:
        my_list = []
        for c in range(len(line)):
            my_int = 0
            if line[c] == '*':
                my_int = 0
            if line[c] == ' ':
                my_int = 1
            if line[c] == 'A':
                my_int = 2
            if line[c] == 'B':
                my_int = 3
            my_list.append(my_int)
        x.append(my_list)
    arr = np.array(x)
    # Once done we'll return the 2D numpy array
    return arr


def find_start(maze):
    # Simple 2D loop to find the starting position 2 (A)
    for rows in range(len(maze)):
        start = []
        for columns in range(len(maze[rows])):
            if maze[rows][columns] == 2:
                start.append(rows)
                start.append(columns)
                return start


def check_valid(maze, i, j, path):
    # reads the char in the path and moves it according to N, S, E, W
    for c in path:
        if c == 'W':
            i -= 1
        elif c == 'E':
            i += 1
        elif c == 'N':
            j -= 1
        elif c == 'S':
            j += 1

        # Makes sure we don't go out of bounds or hit a wall if we do returns False
        if not 0 <= i < len(maze[0]) and 0 <= j < len(maze) or maze[j][i] == 0:
            return False

    # If all is well we'll return True
    return True


def find_solution(maze, i, j, path):
    # reads the char in the path and moves it according to N, S, E, W
    for c in path:
        if c == 'W':
            i -= 1
        elif c == 'E':
            i += 1
        elif c == 'N':
            j -= 1
        elif c == 'S':
            j += 1

    # If we hit 3 (B) we are done so return true
    if maze[j][i] == 3:
        return True

    # We are obviously not done so we return false to keep going
    return False


def print_solution(i, j, maze_txt, solution):
    f = open(maze_txt, 'r')
    maze_list = []
    for line in f:
        maze_list.append(line)

    # A set that will later contain all of the i and j's that we have travelled through
    pos = set()

    # Looping though are solution except the last Char because otherwise we'll overwrite B with a dot
    for c in solution[:-1]:
        if c == 'W':
            i -= 1
        elif c == 'E':
            i += 1
        elif c == 'N':
            j -= 1
        elif c == 'S':
            j += 1
        pos.add((j, i))  # Add i and j to the set as a tuple

    # Printing all of the solutions (String and maze with "graph")
    print('Found: ' + solution)
    print('Maze: ')
    print(' ', end='')
    for j, row in enumerate(maze_list):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print('• ', end='')
            else:
                print(col + ' ', end='')


def solve(txt_file):
    # BFS Algorithm using a standard Queue
    # A queue to hold all of the paths due to this Algo being BFS the first to find B will also be the shortest
    q = queue.Queue()
    q.put('')  # Initialising the queue with an empty string
    path = ''  # Initialising the solution with an empty String
    maze = read_maze(txt_file)  # Reading the maze from the txt file
    pos_list = find_start(maze)  # Finding 2 (A)
    x = pos_list[1]
    y = pos_list[0]

    while not find_solution(maze, x, y, path):  # As long as we have't found 3 (B) we'll keep looping
        path = q.get()  # Dequeue
        for i in ['W', 'E', 'N', 'S']:  # Going through all 4 option each time
            new = path + i  # new being a new possible path
            if check_valid(maze, x, y, new):  # only use it if it's valid though
                if len(new) < 3:  # If it's length is below three backtracking won't hurt the performance at all
                    q.put(new)
                else:  # Making sure we don't fully backtrack each time we don't want this to take an hour
                    if new[-1] == 'W' and new[-2] != 'E' or new[-1] == 'E' and new[-2] != 'W' or new[-1] == 'N' and \
                            new[-2] != 'S' or new[-1] == 'S' and new[-2] != 'N':
                        q.put(new)
    # After we have found the solution the path we now have is also the shortest you can get
    print_solution(x, y, txt_file, path)


# To run the program
solve('maze-zero.txt')

