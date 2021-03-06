import queue
import numpy as np

from os import path

# Sources used except python documentation:
# https://numpy.org/doc/
# https://techwithtim.net/tutorials/breadth-first-search/
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/


def read_maze(src):
    """
    Function to read the txt file and convert it to a numpy 2D array
    :param src: a txt file containing a maze
    :return: a numpy 2D array
    """
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
    """
    Simple 2D loop to find the starting position 2 (A)
    :param maze: a 2D numpy array
    :return: a list where list[0] is i and list[1] is j
    """
    for rows in range(len(maze)):
        start = []
        for columns in range(len(maze[rows])):
            if maze[rows][columns] == 2:
                start.append(rows)
                start.append(columns)
                return start


def check_valid(maze, i, j, path):
    """
    Reads the char in the path and moves it according to N, S, E, W
    :param maze: a 2D numpy array
    :param i: position int
    :param j: position int
    :param path: a String such as SSSEEEWENS containing the instructions for navigating the maze
    :return: a boolean if the path is valid
    """
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
    """
    Reads the char in the path and moves it according to N, S, E, W
    :param maze: a 2D numpy array
    :param i: position int
    :param j: position int
    :param path: a String such as SSSEEEWENS containing the instructions for navigating the maze
    :return: a boolean either True if we hit 3 (B) or False if we have not
    """
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
    """
    Prints out the path (solution) and the input maze with a Path drawn in
    :param i: position int
    :param j: position int
    :param maze_txt: a txt file containing a maze
    :param solution: The path that leads us from A to B
    :return: None
    """
    f = open(maze_txt, 'r')
    maze_list = []
    for line in f:
        maze_list.append(line)

    # A set that will later contain all of the i and j's (positions) that we have travelled through
    pos = set()

    # Looping through our solution except the last Char because otherwise we'll overwrite B with a dot
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
    """
    BFS Algorithm using a standard Queue
    :param txt_file: a txt file containing a maze
    :return: None
    """
    q = queue.Queue()  # A queue to hold all of the paths due to this Algorithm being BFS the first to find B will also
    # be the shortest
    q.put('')  # Initialising the queue with an empty string
    path = ''  # Initialising the solution with an empty String
    maze = read_maze(txt_file)  # Reading the maze from the txt file
    pos_list = find_start(maze)  # Finding 2 (A)
    x = pos_list[1]
    y = pos_list[0]

    while not find_solution(maze, x, y, path):  # As long as we have't found 3 (B) we'll keep looping
        path = q.get()  # Dequeue
        for c in ['W', 'E', 'N', 'S']:  # Going through all 4 option each time
            new = path + c  # new being a new possible path
            if check_valid(maze, x, y, new):  # only use it if it's valid though
                if len(new) < 3:  # If it's length is below three backtracking won't hurt the performance at all
                    q.put(new)
                else:  # Making sure we don't fully backtrack each time we don't want this to take an hour
                    if new[-1] == 'W' and new[-2] != 'E' or new[-1] == 'E' and new[-2] != 'W' or new[-1] == 'N' and \
                            new[-2] != 'S' or new[-1] == 'S' and new[-2] != 'N':
                        q.put(new)
    # After we have found the solution the path we now have is also the shortest you can get
    print_solution(x, y, txt_file, path)


def ask_user(n):
    """
    A simple recursive function that will ask the user for a file name and then solve said file. Has some exception
    handling built in by checking if it is a valid file that the user has entered
    :param n: A simple parameter to check if this is the first time the user has used the program, if so greet him/her
    :return: None
    """
    if n == 'y':  # Greeting depending on whether the program just opened or the loop is being reused
        print('Please enter the name of the file you want to solve: ')
    else:
        print('Hi and welcome to this maze solver,\nPlease enter the name of the file you want to solve: ')
    file = input()
    if not path.exists(file):  # Checking if the file even exists
        print('That is not a valid file. Check that the file you are trying to solve is a maze and located in '
              'this directory')
        ask_user('y')
    solve(file)
    print('\n\nTo solve another maze enter y. If you do not want to solve another one simply press enter')
    user_input = input()
    if user_input == 'y':
        ask_user('y')  # Recursive call to this function with param y to not greet the user again
    else:
        exit()  # If anything other than y is entered then the program will exit


# To run the program
ask_user('')



