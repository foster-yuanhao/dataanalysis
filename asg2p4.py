# -*- coding: utf-8 -*-
"""
Spyder 

"""

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np 
weight = [84,62,78,56,82,55]
calorie = np.array([[1100,1225,1359,1600,1750,1482,1700],
                    [1700,900,1211,1203,1023,900,1322],
                    [1191,1280,1740,1360,1402,1342,1340],
                    [676,567,1094,830,747,781,941],
                    [1356,1289,1368,1147,1204,1301,1356],
                    [1175,1341,1387,1321,1553,1336,1548]])
activitie = [2142, 2142, 1869, 2282, 1869, 1869]

totalCalorie = calorie.sum(axis=1)
x = weight
y = totalCalorie
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunction(x):return slope * x + intercept
mymodel = list(map(myfunction, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.title(r'$correlation\ between\ calories\ intake\ and\ weight\ of\ students$', fontsize=10)
plt.xlabel('weight (kg)')
plt.ylabel('total calories intake')
plt.show()

x1 = weight
y1 = activitie
slope, intercept, r, p, std_err = stats.linregress(x1, y1)
def myfunction(x):return slope * x + intercept
mymodel = list(map(myfunction, x1))
plt.scatter(x1, y1)
plt.plot(x1, mymodel)
plt.title(r'$correlation\ between\ physical\ activities\ and\ weight\ of\ students$', fontsize=10)
plt.xlabel('weight (kg)')
plt.ylabel('physical activities')
plt.show()

x2 = totalCalorie
y2 = activitie
slope, intercept, r, p, std_err = stats.linregress(x2, y2)
def myfunction(x):return slope * x + intercept
mymodel = list(map(myfunction, x2))
plt.scatter(x2, y2)
plt.plot(x2, mymodel)
plt.title(r'$correlation\ between\ physical\ activities\ and\ calorie\ intakes$', fontsize=10)
plt.xlabel('total calories intake')
plt.ylabel('physical activities')
plt.show()