import epidemicmodelling.mobility.network as network
import epidemicmodelling.mobility.flow as flow

import epidemicmodelling.population.population as population

import epidemicmodelling.epidemic.initialcontagion as contagion
import epidemicmodelling.epidemic.model as model

import epidemicmodelling.postprocessing as pp

import numpy as np
import json
import time


def main():
    # Network param.
    NETWORKSIZE = 12
    # Population param.
    PATH = 'C:/Users/victo/Desktop/PythonProjects/EpidemicModelling/epidemicmodelling/data/france.json'
    # Model param.
    k = 5
    ptrans = 0.2
    gamma = 5
    # Simulation param.
    initial_infected = 5
    start_node = 0
    steps = 70

    # Extracts informations from population json file
    population_stats = {}
    with open(PATH) as json_file:
        data = json.load(json_file)
        for p in data:
            population_stats[p['id']] = p

    # Network generation
    net = network.Network()
    x, y, edges = net.france()
    edges = 100 * edges
    # Population generation
    pop = population.Population(population_stats, NETWORKSIZE)
    habitants = pop.generate()

    # Initialize state of infection
    cont = contagion.InitialContagion(habitants, initial_infected, start_node, NETWORKSIZE)
    state_array, habitants = cont.initialise()

    # Flow simulation & contagion on n steps
    S = np.zeros([NETWORKSIZE, steps])
    I = np.zeros([NETWORKSIZE, steps])
    R = np.zeros([NETWORKSIZE, steps])

    Disease = model.SIR(habitants, state_array, k, ptrans, gamma)
    F = flow.WeightedFlow(edges, habitants, state_array)
    for i in range(steps):
        F.popFlow()
        Disease.globalspread()

        for j in range(NETWORKSIZE):
            S[j][i] = state_array[j][1]
            I[j][i] = state_array[j][2]
            R[j][i] = state_array[j][3]

    # Display
    plot = pp.DisplaySIR(steps, NETWORKSIZE, S, I, R)
    analysis = pp.StatisticsSIR(steps, NETWORKSIZE, S, I, R)
    plot.plot_global()
    plot.plot_infected()
    for i in range(NETWORKSIZE):
        peak, time = analysis.local_infection_peak(i)
        print(f'Infected in node {i} peaked at {peak} on day {time}')
        print('----------------------------------------------------')

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
