import numpy as np


def read_maze(src):
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
    # Columns print(len(arr))
    # Rows print(len(arr[0]))
    return arr


def find_start(arr):
    for rows in range(len(arr)):
        start = []
        for columns in range(len(arr[rows])):
            if arr[rows][columns] == 2:
                start.append(rows)
                start.append(columns)
                return start


def find_route(arr):
    starting_position = find_start(arr)
    print(starting_position)


def main():
    find_route(read_maze('maze-one.txt'))


if __name__ == "__main__":
    main()