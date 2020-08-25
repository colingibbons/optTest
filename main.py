import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from timer import Timer


# define a test function
def testFunction(x, y):
    output = (x**2) + (y**2)
    return output

# initialize timer object
t = Timer()

# initialize plot
fig = plt.figure()
ax = plt.axes(projection='3d')

# generate test data set
x = np.linspace(-10, 10, 21)
y = np.linspace(-10, 10, 21)
X, Y = np.meshgrid(x, y)
Z = testFunction(X, Y)

# display basic statistics for data set
print("Test data generation complete. Here's some stats about the data:")
print("Number of points: " + str(len(Z)))
print("Minimum Value: " + str(np.min(Z)))
print("Maximum Value: " + str(np.max(Z)))
print("Average Value: " + str(np.mean(Z)))

# generate plot for data set
ax.plot_surface(X, Y, Z)

# title and axis labels
ax.set_title('3D Plot of Objective Function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# display the plot
plt.show()
# define optimization object
#res = opt.minimize(testFunction, x, y, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})
