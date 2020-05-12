import math
import numpy as np
import scipy.stats

class Network:
    def __init__(self):
        pass

    def poisson(self,xmin, xmax, ymin, ymax,lambda0: int,connect_dist: float):
        xdelta = xmax - xmin
        ydelta = ymax - ymin  # rectangle dimensions
        area_total = xdelta * ydelta

        numbPoints = scipy.stats.poisson(lambda0 * area_total).rvs()  # Poisson number of points
        x = xdelta * scipy.stats.uniform.rvs(0, 1, (numbPoints, 1)) + xmin  # x coordinates of Poisson points
        y = ydelta * scipy.stats.uniform.rvs(0, 1, (numbPoints, 1)) + ymin  # y coordinates of Poisson points

        edges = self._edges(x,y,connect_dist)

        return x,y,edges

    @staticmethod
    def france():
        x = [0.71, 0.86, 1, 0.71, 0.57, 0.58, 0.56, 0.14, 0.29, 0.05, 0, 0.71]
        y = [0, 0.33, 0.56, 1, 0.11, 0.44, 0.78, 0.22, 0.74, 0.33, 0.81, 0.44]
        edges = np.array([[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                          [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                          [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                          [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                          [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                          [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                          [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
        return x,y,edges

    def _edges(self,x,y,connect_dist):
        n = len(x)
        edges = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                if self._dist(x[i], y[i], x[j], y[j])<=connect_dist:
                    edges[i][j]=1
        return edges

    @staticmethod
    def _dist(x1,y1,x2,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
