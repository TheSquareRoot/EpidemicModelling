import numpy.random as rd
from abc import abstractmethod


class CompartmentalModel:
    def __init__(self,habitants,state_list):
        self.habitants = habitants
        self.state_list = state_list

    @abstractmethod
    def globalspread(self):
        """Spread during one time step in all nodes"""
        pass

    @abstractmethod
    def localspread(self,habitants,state):
        """Spread during one time step in a closed population"""
        pass

class SIR(CompartmentalModel):
    """
    For practical purposes, differents states are represented by integers
    susceptible : 1
    infected    : 2
    recovered   : 3
    It corresponds to their line number in the state list
    """
    def __init__(self,habitants,state_list,k,ptrans,gamma):
        super().__init__(habitants,state_list)
        self.k = k           # Average number of contacts per day
        self.ptrans = ptrans # Probability of transmission
        self.gamma = gamma   # Recovery rate

    def globalspread(self):
        for i in range(len(self.habitants)):
            self.state_list[i] = self.localspread(self.habitants[i],self.state_list[i])

    def localspread(self,local_habitants,state):
        N,S,I,R = state[0],state[1],state[2],state[3]
        newS,newI,newR = S,I,R
        for a in local_habitants:
            if a.state == 1: # Susceptible agent
                p = 1-(1-self.ptrans)**(self.k*I/N) # Probability of getting infected
                if rd.binomial(1,p)==1:
                    a.state = 2
                    newI+=1
                    newS-=1
            if a.state == 2: # Infected agent
                if rd.binomial(1,1/self.gamma)==1:
                    a.state = 3
                    newI-=1
                    newR+=1
        state[1],state[2],state[3] = newS,newI,newR
        return state
