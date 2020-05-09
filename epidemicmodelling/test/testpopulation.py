import epidemicmodelling.population.population as population

import matplotlib.pyplot as plt
import numpy as np

P = population.Population(13)

habitants = P.generate()

population_by_group = np.zeros([5,13])

for localhabs in habitants:
    for a in localhabs:
        pos = a.position
        age = a.age
        if 0<=age<=19:
            population_by_group[0,pos]+=1
        if 20<=age<=39:
            population_by_group[1,pos]+=1
        if 40<=age<=59:
            population_by_group[2,pos]+=1
        if 60<=age<=74:
            population_by_group[3,pos]+=1
        if age>=75:
            population_by_group[4,pos]+=1

tot_population_by_group = [0,0,0,0,0]

for i in range(5):
    for j in range(13):
        tot_population_by_group[i]+=population_by_group[i,j]

print(population_by_group)
print(tot_population_by_group)
