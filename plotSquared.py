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
    counter = 0;
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
    sum = 0
    for i in d:
        sum += i
    return sum/d.size

def xxxxAvg(d):
    sum = 0
    counter = 0
    for i in d:
        sum += math.pow(counter,4)
        counter += 1
    return sum/d.size

def xxyAvg(d):
    sum = 0
    counter = 0
    for i in d:
        sum += i*math.pow(counter,2)
        counter += 1
    return sum/d.size

def xxxAvg(d):
    sum = 0
    counter = 0
    for i in d:
        sum += math.pow(counter,3)
        counter += 1
    return sum/d.size

fig1 = plt.figure()

dataNum = 10
d = 20*np.random.rand(dataNum, 1)#10=x&y limit and # of points. 3=# of points * 3     

xAvg = xAvg(d) #x avg
xxAvg = xsAvg(d) #x^2 avg
xyAvg = xyAvg(d) #xy avg
yAvg = yAvg(d) #y avg

xxxAvg=xxxAvg(d)

xxxxAvg=xxxxAvg(d)
xxyAvg=xxyAvg(d)
#y=Bx^2+Ax+C

A=((xyAvg-xAvg*yAvg)*(xxxxAvg-xxAvg*xxAvg)-(xxyAvg-xxAvg*yAvg)*(xxxAvg-xAvg*xxAvg))/((xxAvg-xAvg*xAvg)*(xxxxAvg-xxAvg*xxAvg)-(xxxAvg-xAvg*xxAvg)*(xxxAvg-xAvg*xxAvg))
B=((xxyAvg-xxAvg*yAvg)*(xxAvg-xAvg*xAvg)-(xyAvg-xAvg*yAvg)*(xxxAvg-xAvg*xxAvg))/((xxAvg-xAvg*xAvg)*(xxxxAvg-xxAvg*xxAvg)-math.pow(xxxAvg-xAvg*xxAvg,2))
C=yAvg-A*xAvg-B*xxAvg


z = np.arange(-100,100,1)
plt.ylim(-100,100)
plt.xlim(-100,100)

z = np.arange(-10,100,1)
plt.ylim(-5,30)
plt.xlim(-5,20)
ax = plt.plot(d,'go') #'Go' displays the datapointsax = plt.plot(z,C*z*z+B*z+A)
ax = plt.plot(z,B*z*z+A*z+C)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Regression')
plt.show()
