
import numpy as np
import matplotlib.pyplot as plt
import math


def xyAvg(d):#assumes that x increments as an integer
    sum = 0.0
    counter = 0
    for i in d:
        sum += i*counter
        counter += 1
    return sum/d.size

def xAvg(d):#assumes that x increments as an integer
    sum = 0
    counter = 0
    for i in d:
        sum += counter
        counter += 1
    return sum/d.size

def xsAvg(d):#x squared avg, assumes that x increments as an integer
    sum = 0.0
    counter  = 0
    for i in d:
        sum += math.pow(counter,2)
        counter += 1
    return sum/d.size

def yAvg(d):
    sum = 0.0
    for i in d:
        sum += i
    return sum/d.size

fig1 = plt.figure()

dataNum = 10
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. Right parameter = how many points per x value
xAvg = xAvg(d) #x avg
xsAvg = xsAvg(d) #x^2 avg
xyAvg = xyAvg(d) #xy avg
yAvg = yAvg(d) #y avg
slope = (xAvg*yAvg-xyAvg)/(math.pow(xAvg,2)-xsAvg)

print(d)
print("x average: ", xAvg, "\nx-squared average: ", xsAvg, "\nxy average: ", xyAvg, "\ny average: ", yAvg)
print("slope =",slope)

yIntercept = yAvg-slope*xAvg
print("Y-int = ",yIntercept)
z = np.arange(-10,100,1)
ax = plt.plot(d,'go') #'Go' displays the datapoints
ax = plt.plot(z,z*slope+yIntercept)
plt.xlim(-1, 10)
plt.ylim(-5,10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')

plt.show()