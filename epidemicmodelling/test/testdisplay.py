import epidemicmodelling.postprocessing as display

import numpy as np

def main():
    # Display arguments
    x = [0, 2]
    y = [0, 2]
    edges = np.ones([2,2])
    steps = 10
    NETWORKSIZE = 2
    # State lists through time
    S = 0
    I = np.array([[0, 0,  5, 20, 33, 38, 21, 10, 5, 2],
                  [5, 7, 23, 40, 42, 35, 20,  8, 3, 0]])
    print(I[0,5])
    print("oooooooo")
    R = 0
    # Display
    Graph = display.DisplaySIR(x, y ,edges, steps, NETWORKSIZE, S, I, R)
    Graph.graph()

if __name__ == '__main__':
    main()