import time

from epidemicmodelling.mobility import network
import epidemicmodelling.population.population as population
import epidemicmodelling.mobility.flow as flow
import epidemicmodelling.epidemic.model as model

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Network generation
    net = network.Network()
    x, y, edges = net.france()
    # Population generation
    habitants = []
    for i in range(12):
        pop = population.Population(i,1000)
        habitants.append(pop.generate())
    print(habitants)
    # Generate of initial state of infection
    state_list = []
    for _ in range(12):
        state_list.append([1000,1000,0,0])
    state_list[0][1]=995
    state_list[0][2]=5
    habitants[0][0].state = 2
    habitants[0][1].state = 2
    habitants[0][2].state = 2
    habitants[0][3].state = 2
    habitants[0][4].state = 2

    # Flow simulation on n-steps
    steps  = 50
    k      = 5
    ptrans = 0.2
    gamma  = 5

    Disease = model.SIR(habitants, state_list, k, ptrans, gamma)
    F = flow.WeightedFlow(edges,habitants,state_list)
    print(state_list)

    S = np.zeros([12,steps])
    I = np.zeros([12, steps])
    R = np.zeros([12, steps])
    for i in range(steps):
        F.popFlow()
        Disease.globalspread()
        print(state_list)

        for j in range(12):
            S[j][i]=state_list[j][1]
            I[j][i] = state_list[j][2]
            R[j][i] = state_list[j][3]

    # Display
    x = [i for i in range(steps)]
    S1 = [S[0][i] for i in range(steps)]
    I1 = [I[0][i] for i in range(steps)]
    R1 = [R[0][i] for i in range(steps)]

    S2 = [S[4][i] for i in range(steps)]
    I2 = [I[4][i] for i in range(steps)]
    R2 = [R[4][i] for i in range(steps)]

    S3 = [S[8][i] for i in range(steps)]
    I3 = [I[8][i] for i in range(steps)]
    R3 = [R[8][i] for i in range(steps)]

    S4 = [S[10][i] for i in range(steps)]
    I4 = [I[10][i] for i in range(steps)]
    R4 = [R[10][i] for i in range(steps)]

    fig, a = plt.subplots(2, 2)

    a[0, 0].plot(x, S1, color='g')
    a[0, 0].plot(x, I1, color='r')
    a[0, 0].plot(x, R1, color='y')
    a[0, 0].set_title('Ville 0')

    a[0, 1].plot(x, S2, color='g')
    a[0, 1].plot(x, I2, color='r')
    a[0, 1].plot(x, R2, color='y')
    a[0, 1].set_title('Ville 4')

    a[1, 0].plot(x, S3, color='g')
    a[1, 0].plot(x, I3, color='r')
    a[1, 0].plot(x, R3, color='y')
    a[1, 0].set_title('Ville 8')

    a[1, 1].plot(x, S4, color='g')
    a[1, 1].plot(x, I4, color='r')
    a[1, 1].plot(x, R4, color='y')
    a[1, 1].set_title('Ville 10')

    plt.show()

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
