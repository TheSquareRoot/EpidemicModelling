import epidemicmodelling.mobility.randomwalk as rw

from abc import abstractmethod
import random

# TODO: add two flow layers, one for airplane and one for commuting
# TODO: add dynamic flows

class Flow:
    def __init__(self,edges,habitants,state_list):
        self.edges = edges
        self.habitants = habitants
        self.state_list = state_list

    def getPopulation(self,i):
        # Returns population of node i
        return len(self.habitants[i])

    def getTotalPopulation(self):
        # Returns total population of network
        tot = 0
        for i in range(len(self.habitants)):
            tot += len(self.habitants[i])
        return tot

    def getPopulationList(self):
        # Returns a list with the population of each node
        population = []
        for i in range(len(self.habitants)):
            population.append(len(self.habitants[i]))
        return population

    @abstractmethod
    def popFlow(self):
        pass

    @abstractmethod
    def nextStep(self):
        """Gives all agents their next destination in the network"""
        pass

    @abstractmethod
    def newPopulation(self):
        """Updates the population of each node by moving agents to their destination"""
        pass

class RandomFlow(Flow):
    def popFlow(self):
        print(self.getPopulationList())
        self.habitants = self.newPopulation()
        print(self.getTotalPopulation())

    def nextStep(self) -> list:
        travellers = []
        for i in range(len(self.habitants)):
            for a in self.habitants[i]:
                walk = rw.RandomWalk(1,self.edges)
                a.prevposition = a.position
                a.position = walk.nextNode(a.position)
                travellers.append(a)
        return travellers

    def newPopulation(self) -> list:
        newhabs = self.habitants
        travellers = self.nextStep()
        for a in travellers:
            newhabs[a.prevposition].remove(a)
            newhabs[a.position].append(a)
        return newhabs

class WeightedFlow(Flow):
    def popFlow(self):
        self.habitants,self.state_list = self.newPopulation()

    def nextStep(self) -> list:
        travellers = []
        for i in range(len(self.habitants)):
            for j in range(len(self.edges[i])):
                counter = 0
                while counter<self.edges[i][j]:
                    a = random.choice(self.habitants[i])
                    if a not in travellers:
                        a.prevposition = a.position
                        a.position = j
                        travellers.append(a)
                        counter+=1
        return travellers

    def newPopulation(self) -> tuple:
        newhabs = self.habitants
        newstates = self.state_list
        travellers = self.nextStep()
        for a in travellers:
            # Updating habitants
            newhabs[a.prevposition].remove(a)
            newhabs[a.position].append(a)
            # Updating state_list
            newstates[a.prevposition][a.state]-=1
            newstates[a.position][a.state] += 1
        return newhabs,newstates
