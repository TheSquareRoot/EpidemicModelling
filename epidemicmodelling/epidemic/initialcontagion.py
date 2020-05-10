import numpy as np

# TODO: generalize
# TODO: initial infected can't be kids (to be discussed)

class InitialContagion:
    def __init__(self, habitants, initial_infected, start_node, NETWORKSIZE):
        self.habitants = habitants
        self.initial_infected = initial_infected
        self.start_node = start_node
        self.NETWORKSIZE = NETWORKSIZE

    def initialise(self):
        state_array = np.zeros(self.NETWORKSIZE, 4)
        new_habitants = self.habitants
        # Generates initial state_array
        for i in range(self.NETWORKSIZE):
            state_array[i, 0] = 100
            state_array[i, 1] = 100
        state_array[self.start_node, 1]-=self.initial_infected
        state_array[self.start_node, 2]=self.initial_infected
        # Update agents' states
        for i in range(self.initial_infected):
            self.habitants[self.start_node][i].state = 2
        return state_array, new_habitants
