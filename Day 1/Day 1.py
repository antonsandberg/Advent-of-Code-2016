import numpy as np
from numpy import pi, sin, cos


def process_data(FILENAME):
    with open(FILENAME) as f:
        data =[x.strip(',') for x in f.read().split()]
    for i, dat in enumerate(data):
        data[i] = (dat[0], int(dat[1:]))
    return data

def main():
    FILENAME = 'Day 1\small_input.txt'
    data = process_data(FILENAME)

    print(np.sin(pi/2))
    
    


if __name__ == '__main__':
    main()

