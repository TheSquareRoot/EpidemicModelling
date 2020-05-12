import epidemicmodelling.population.agent as agent

import random
import json
import math

# TODO: method that returns the population for each node

class Population:
    def __init__(self, population_stats, NETWORKSIZE):
        self.population_stats = population_stats # Population percentage in each age group for each node
        self.NETWORKSIZE = NETWORKSIZE # Number of nodes

    def generate(self):
        # Populates the network with agents
        habitants = []
        for i in range(self.NETWORKSIZE):
            localhabs = []
            # SIZE = self.population_stats[i]['size']
            SIZE = 1000
            # Computes size of each age group from total population
            GROUP1SIZE = math.floor(self.population_stats[i]['0to19'] * SIZE / 100)
            GROUP2SIZE = math.floor(self.population_stats[i]['20to39'] * SIZE / 100)
            GROUP3SIZE = math.floor(self.population_stats[i]['40to59'] * SIZE / 100)
            GROUP4SIZE = math.floor(self.population_stats[i]['60to74'] * SIZE / 100)
            GROUP5SIZE = SIZE - GROUP1SIZE - GROUP2SIZE - GROUP3SIZE - GROUP4SIZE
            # Generates agents for each age group and adds them to the local population
            for _ in range(GROUP1SIZE):
                localhabs.append(self.generateAgent(0, 19, i))
            for _ in range(GROUP2SIZE):
                localhabs.append(self.generateAgent(20, 39, i))
            for _ in range(GROUP3SIZE):
                localhabs.append(self.generateAgent(40, 59, i))
            for _ in range(GROUP4SIZE):
                localhabs.append(self.generateAgent(60, 74, i))
            for _ in range(GROUP5SIZE):
                localhabs.append(self.generateAgent(75, 90, i))
            habitants.append(localhabs)
        return habitants

    @staticmethod
    def generateAgent(min_age, max_age, position):
        # Randomly generates an agent within the given age range in the given node
        age = random.randint(min_age, max_age)
        sex = random.choice(['m', 'f'])
        position = position
        state = 1
        return agent.Agent(age, sex, position, state)
