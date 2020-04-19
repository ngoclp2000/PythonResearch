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

def generate_synth_data(n=50):
    """ Create two sets of points from bivariate normal distributions. """
    points = np.concatenate((ss.norm(0,1).rvs((n,2)) , ss.norm(1,1).rvs((n,2))),axis= 0)
    outcomes = np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return (points,outcomes)
n = 20
points, outcomes = generate_synth_data(n)
plt.figure()
plt.plot(points[:n,0] , points[:n,1] , "ro")
plt.plot(points[n:,0] , points[n:,1], "bo")
plt.savefig("bivariate.pdf")

def make_prediction_grid(predictors,outcomes,limits,h,k):
    """ Classify each point on the prediction grid. """
    (x_min, x_max , y_max , y_min) = limits
    xs = np.arange(x_min, x_max , h)
    ys = np.arange(y_min, y_max, h)
    xx , yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype= int )
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    
    return (xx, yy, prediction_grid)