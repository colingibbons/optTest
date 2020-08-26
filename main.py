import numpy as np
# import scipy.optimize as opt
import cvxopt as cvx
import testFunctions as test
from timer import Timer

# initialize timer object
t = Timer()

# define necessary variables
x = []
y = []
x.append([100, 100])
y.append([100, 300])

# start the timer
t.start()

# code to best tested goes here
resultOne = test.squaredEuclideanOne(x, y)
print(resultOne)

#stop the timer
t.stop()

# start a second timer
t.start()

resultTwo = test.squaredEuclideanTwo(x, y)
print(resultTwo)

# stop the timer
t.stop()


