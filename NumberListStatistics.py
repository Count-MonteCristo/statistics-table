#!/usr/bin/python
#File Name: NumberListStatistics.py
#Author: Luis Navarro

#Imports
from datetime import datetime
import time
import random
import statistics

#Header
print("-------------------------------------------------")
print("Statistics of Randomly generated 1000 Number List")
print("           Developer: Luis Navarro               ")
print("        Prepared on : %s" % (time.strftime('%Y-%m-%d %H:%M:%S') ))
print("-------------------------------------------------")

#List where the random numbers will be stored
numberList = []

#Creating the 1000 random numbers using a loop and adding them to the list
for i in range(1000):
    r = random.randint(1,100)
    numberList.append(r)

#Output - total elements
listElements = len(numberList)
print("List has " + str(listElements) + " elements.")

#Output - sum
listSum = sum(numberList)
print("Sum of all elements in list is: " + str(listSum))

#Output - max
listMax = max(numberList)
print("List has a Maximum value of " + str(listMax))

#Output - min
listMin = min(numberList)
print("List has a Maximum value of " + str(listMin))

#Output - mean
listMean = statistics.mean(numberList)
print("Mean of " + str(listElements) + " elements in the list is: " + str(listMean))

#Output - median
listMedian = statistics.median(numberList)
print("Median of " + str(listElements) + " elements in the list is: " + str(listMedian))

#Output - even and odd
even = 0
odd = 0

for r in numberList: 
    if r % 2 == 0: 
        even += 1
    else: 
        odd += 1

print("List has " + str(even) + " even elements.")
print("List has " + str(odd) + " odd elements.")

#Output - elements within a range
range1 = 0 #1 - 25
range2 = 0 #26 - 50
range3 = 0 #51 - 75
range4 = 0 #76 - 100

for r in numberList:
    if r <= 25:
        range1 += 1
    elif r > 25 and r <= 50:
        range2 += 1
    elif r > 50 and r <= 75:
        range3 += 1
    else:
        range4 += 1
        
print("List has " + str(range1) + " elements between 1 and 25.")
print("List has " + str(range2) + " elements between 26 and 50.")
print("List has " + str(range3) + " elements between 51 and 75.")
print("List has " + str(range4) + " elements between 76 and 100.")

#Footer
print("-------------------------------------------------")
