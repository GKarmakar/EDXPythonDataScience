import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.style.use('ggplot') # Look pretty
from mpl_toolkits.mplot3d import Axes3D

concrete = pd.read_csv("concrete.csv")

fig = plt.figure()
plt.suptitle('Cement x H2O x Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("Cement Content")
ax.set_ylabel("Water Content")
ax.set_zlabel('Concrete Strength')
ax.scatter(concrete.Cement, concrete.Water, c='r', marker='o')

fig = plt.figure()
plt.suptitle('Cement x Slag x Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("Cement Content")
ax.set_ylabel("Slag Content")
ax.set_zlabel('Concrete Strength')
ax.scatter(concrete.Cement, concrete.Superplasticizer, c='g', marker='o')

fig = plt.figure()
plt.suptitle('Cement x FlyAsh x Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel("Cement Content")
ax.set_ylabel("FlyAsh Content")
ax.set_zlabel('Concrete Strength')
ax.scatter(concrete.Cement, concrete.FlyAsh, c='g', marker='o')

plt.show()