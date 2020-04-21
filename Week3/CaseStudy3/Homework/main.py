import numpy as np, random, scipy.stats as ss, pandas as pd

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

dataframe = pd.read_csv("../../../FileCSV/file1.csv", 
                      index_col=0)

dataframe['is_red'] = (dataframe['color'] == 'red').astype(int)
numeric_data = dataframe.drop('color', axis = 1)
#print(numeric_data[0:5].is_red)
scaled_data = numeric_data.scale()
#numeric_data = 