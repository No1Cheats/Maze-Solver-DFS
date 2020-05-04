import numpy as np


def read_maze(src):
    f = open(src, 'r')

    #arr = np.array([], np.int32)
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
        print(list)


def main():
    read_maze('maze-one.txt')


if __name__ == "__main__":
    main()