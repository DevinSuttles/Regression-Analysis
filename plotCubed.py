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
    sum = 0.0
    for i in d:
        sum += 1
    return sum/d.size

def xsAvg(d):#x squared avg, assumes that x increments as an integer
    sum = 0.0
    counter  = 0
    for i in d:
        sum += math.pow(counter,2)
        counter += 1
    return sum/d.size

def yAvg(d):
    sum = 0
    for i in d:
        sum += i
    return sum/d.size

fig1 = plt.figure()

dataNum = 10
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. 3=# of points * 3     

xAvg = xAvg(d) #x avg
xsAvg = xsAvg(d) #x^2 avg
xyAvg = xyAvg(d) #xy avg
yAvg = yAvg(d) #y avg
xxAvg=xAvg*xsAvg
#y=Ax^2+Bx+C
B=(xAvg*yAvg*math.pow(xAvg,4)-xsAvg*yAvg*math.pow(xAvg,3))/(math.pow(xAvg,6)-math.pow(xxAvg,2))
C=(xsAvg*yAvg*xsAvg-xAvg*yAvg*xxAvg)/(math.pow(xAvg,6)-math.pow(xxAvg,2))
A=yAvg-B*xAvg-C*xsAvg

z = np.arange(0,10,1)
plt.ylim(-5,10)
plt.xlim(-1,11)
ax = plt.plot(d,'go') #'Go' displays the datapoints
ax = plt.plot(z,C*z*z+B*z+A)

