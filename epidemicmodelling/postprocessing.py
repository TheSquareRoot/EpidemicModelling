from abc import abstractmethod

import matplotlib.pyplot as plt
import numpy as np


"""
12/05/2020

This class gathers various displaying methods used to visualise the spread
of the epidemic. It aims to be as extensive as possible to cover all 
potential usage.

@author TheSquareRoot
"""

# TODO: make plot_infected easier to read

class Display:
    def __init__(self, steps, NETWORKSIZE):
        self.steps = steps
        self.NETWORKSIZE = NETWORKSIZE

    @abstractmethod
    def plot_local(self, node):
        """Plots the model evolution through time in one node"""
        pass

    @abstractmethod
    def plot_global(self):
        """Plots the model evolution through time in the network"""
        pass

class DisplaySIR(Display):
    def __init__(self, steps, NETWORKSIZE, *args):
        super().__init__(steps, NETWORKSIZE)
        self.S = args[0]
        self.I = args[1]
        self.R = args[2]

    def plot_local(self, node):
        # Plots S, I and R through time in one node
        S_local = []
        I_local = []
        R_local = []
        for i in range(self.steps):
                S_local.append(self.S[node, i])
                I_local.append(self.I[node, i])
                R_local.append(self.R[node, i])
        # Plot
        t = [ i for i in range(self.steps)]
        plt.plot(t, S_local, color='g')
        plt.plot(t, I_local, color='r')
        plt.plot(t, R_local, color='y')
        plt.show()

    def plot_global(self):
        # Plots S, I and R through time in the total population
        S_global = np.zeros(self.steps)
        I_global = np.zeros(self.steps)
        R_global = np.zeros(self.steps)
        for i in range(self.steps):
            for j in range(self.NETWORKSIZE):
                S_global[i] += self.S[j,i]
                I_global[i] += self.I[j, i]
                R_global[i] += self.R[j, i]
        # Plot
        t = [ i for i in range(self.steps)]
        plt.plot(t, S_global, color='g')
        plt.plot(t, I_global, color='r')
        plt.plot(t, R_global, color='y')
        plt.show()

    def plot_infected(self):
        # Plots I throughs times in all nodes
        t = [ i for i in range(self.steps)]
        # Creates a color scale
        red_value = np.linspace(0,1,self.NETWORKSIZE)
        color = [ (red_value[i], 0, 0) for i in range(self.NETWORKSIZE)]
        # Plot
        for i in range(self.NETWORKSIZE):
            plt.plot(t, self.I[i,:], color=color[i])
        plt.show()

"""
12/05/2020

This class provides methods to better understand and analyse the results of 
the simulation.

@author TheSquareRoot
"""

class Statistics:
    def __init__(self, steps, NETWORKSIZE):
        self.steps = steps
        self.NETWORKSIZE = NETWORKSIZE

class StatisticsSIR(Statistics):
    def __init__(self, steps, NETWORKSIZE, *args):
        super().__init__(steps, NETWORKSIZE)
        self.S = args[0]
        self.I = args[1]
        self.R = args[2]

    def local_infection_peak(self,node):
        # Returns the time of the infection peak and its value in a node
        peak = 0
        time = 0
        for i in range(self.steps):
            if self.I[node, i] > peak:
                peak = self.I[node, i]
                time = i
        return peak, time

    def global_infection_peak(self):
        pass

