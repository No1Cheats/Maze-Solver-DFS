import numpy as np


def read_maze(src):
    f = open(src, 'r')

    arr = np.array([], np.int32)
    x = []
    for line in f:
        list = []
        for c in range(len(line)):
            int = 0
            if line[c] == '*':
                int = 0
            if line[c] == ' ':
                int = 1
            if line[c] == 'A':
                int = 2
            if line[c] == 'B':
                int = 3
            list.append(int)
        x.append(list)
    arr = np.array(x)
    return arr


def main():
    read_maze('test.txt')


if __name__ == "__main__":
    main()