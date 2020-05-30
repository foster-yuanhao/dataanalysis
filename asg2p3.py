# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
#declear the matrix for data
array=[1100,1225,1359,1600,1750,1482,1700,\
        1700,900,1211,1203,1023,900,1322,\
        1191,1280,1740,1360,1402,1342,1340,\
        676,567,1094,830,747,781,941,\
        1356,1289,1368,1147,1204,1301,1356,\
        1175,1341,1387,1321,1553,1336,1548]

print(min(array))
#for min value function
 
print(max(array))
#for max value function

x = numpy.var(array) 
print(x) 
#for Variance in python

x = numpy.std(array)
print(x) 
#for Standard deviation in python 

    
x = numpy.mean(array)
print(x)

import scipy
from scipy import stats

    
x = stats.mode(array)
print(x)
    
#The data set for the first group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [1100,1225,1359,1600,1750,1482,1700] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [1100,1225,1359,1600,1750,1482,1700]
plt.scatter(x, y)
plt.show()

#The data set for the second group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [1700,900,1211,1203,1203,900,1322] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [1700,900,1211,1203,1203,900,1322]
plt.scatter(x, y)
plt.show()


#The data set for the third group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [1191,1280,1740,1360,1402,1342,1340] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [1191,1280,1740,1360,1402,1342,1340]
plt.scatter(x, y)
plt.show()

#The data set for the fourth group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [676,567,1094,830,747,781,941] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [676,567,1094,830,747,781,941]
plt.scatter(x, y)
plt.show()


#The data set for the fifth group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [1356,1289,1368,1147,1204,1301,1356] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [1356,1289,1368,1147,1204,1301,1356]
plt.scatter(x, y)
plt.show()


#The data set for the sixth group member
#The X-axis is the week. 
#The Y-axis is the number of calories consumed per week
x = [4,5,6,7,1,2,3] 
y= [1175,1341,1387,1321,1553,1336,1548] 
import matplotlib.pyplot as plt 
x = [4,5,6,7,1,2,3]
y= [1175,1341,1387,1321,1553,1336,1548]
plt.scatter(x, y)
plt.show()




