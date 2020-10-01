import numpy as np
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import sqeuclidean
from sklearn.metrics.pairwise import euclidean_distances


# function to calculate Euclidean distance between two input vectors from scipy
def euclideanOne(x, y):
    output = euclidean(x, y)
    return output


# function to calculate Euclidean distances from sklearn
def euclideanTwo(x, y):
    output = euclidean_distances()
    return output


# define function for SED
def squaredEuclideanOne(x, y):
    output = float(((x[0][0] - y[0][0])**2) + ((x[0][1] - y[0][1])**2))
    return output


def squaredEuclideanTwo(x, y):
    output = euclidean_distances(x, y, squared=True)
    return output


# this is a facsimile of the contour comparison function in ultrasoundProbe.py in PATS, adapted for testing purposes.
# note that intersectionContours is a polydata object in a PATS context, but here it will likely be handled as a
# list for simplicity's sake
def objectiveFunction(numPoints, intersectionContours, tracedPointsEpi, tracedPointsEndo):
    # initialize variables for accruing Euclidean distance
    totalDistEpi = 0
    totalDistEndo = 0
    objective = 10000
    # loop through each point on the epi
    return objective
