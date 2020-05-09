import random


class RandomWalk:
    def __init__(self,steps,edges):
        self.steps = steps
        self.edges = edges

    def nextNode(self,node: int) -> int:
        #Choses a random neighbour to go to
        neighbours = []
        for i in range(len(self.edges[node])):
            if self.edges[node][i]!=0: neighbours.append(i)
        return random.choice(neighbours)

    def walk(self) -> list:
        #Returns the list of visited nodes during the random walk
        visited = [0]
        current_node = 0
        counter = 0
        while counter<self.steps:
            current_node = self.nextNode(current_node)
            visited.append(current_node)
            counter+=1
        return visited
