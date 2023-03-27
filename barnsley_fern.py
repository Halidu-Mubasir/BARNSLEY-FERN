import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# transformations
def transformation1(x,y):
    return (0, 0.16*y)
def transformation2(x,y):
    return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def transformation3(x,y):
    return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def transformation4(x,y):
    return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)

transformations = [transformation1, transformation2, transformation3, transformation4]
iterations = 100000
width, height = 300, 300 # dimensions of the image window
fern_image = np.zeros((width, height))
x, y = 0, 0 #starting point
for i in range(iterations):
    transformation = np.random.choice(transformations, p = [0.01, 0.85, 0.07, 0.07])# randomly choosing a transformation based on probability
    x, y = transformation(x, y) 
    ix, iy = int(width/2 + x * width/10), int(y * height/12)
    fern_image[iy, ix] = 1
plt.imshow(fern_image[::-1, :], cmap = cm.Greens)
plt.show()