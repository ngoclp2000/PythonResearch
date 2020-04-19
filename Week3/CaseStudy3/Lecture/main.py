import numpy as np 
import scipy.stats as ss
import matplotlib.pyplot as plt
def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2-p1,2)))

def majority_vote(votes):
    mode, count = ss.mstats.mode(votes)
    return mode
def find_nearest_element(p,points, k =5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p,points[i])
    ind = np.argsort(distances)
    print(ind)
    return ind[:k]
def knn_predict(p,points,outcome,k=5):
    idn = find_nearest_element(p,points,k)
    print(outcome[idn])
    return majority_vote(outcome[idn])

points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2,2.5])
outcome = np.array([0,0,0,0,1,1,1,1,1])
print(type(points.shape))