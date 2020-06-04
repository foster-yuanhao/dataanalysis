#We will choose to use the calorie intake of the first and second students for a week to do the hypothesis test
import numpy 
calories = [1100,1225,1359,1600,1750,1482,1700,1700,900,1211,1203,1023,900,1322] 
x = numpy.mean(calories)
print(x)
print ("We know from the second part that the average of the six people is 1248.6.In the hypothesis test, the average of two people is 1319.6, and we can know that the population average of two people is not equal to the population average of six people")