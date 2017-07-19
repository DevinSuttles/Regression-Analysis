import numpy as np
import matplotlib.pyplot as plt
import math

def xyAvgf(d):#assumes that x increments as an integer
    sum = 0.0
    counter = 0
    for i in d:
        sum += i*counter
        counter += 1
    return sum/d.size

def xAvgf(d):#assumes that x increments as an integer
    sum = 0.0
    for i in d:
        sum += 1
    return sum/d.size

def xsAvgf(d):#x squared avg, assumes that x increments as an integer
    sum = 0.0
    counter  = 0
    for i in d:
        sum += math.pow(counter,2)
        counter += 1
    return sum/d.size

def yAvgf(d):
    sum = 0
    for i in d:
        sum += i
    return sum/d.size

def xxxxAvgf(d):
    sum = 0
    counter = 0
    for i in d:
        sum += math.pow(counter,4)
        counter += 1
    return sum/d.size

def xxyAvgf(d):
    sum = 0
    counter = 0
    for i in d:
        sum += i*math.pow(counter,2)
        counter += 1
    return sum/d.size

def xxxAvgf(d):
    sum = 0
    counter = 0
    for i in d:
        sum += math.pow(counter,3)
        counter += 1
    return sum/d.size

fig1 = plt.figure()

<<<<<<< HEAD
dataNum = 30
=======
dataNum = 3
>>>>>>> ef2f4e737d83fa9d410352deb6e548184d4b74c0
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. 3=# of points * 3     

xAvg = xAvgf(d) #x avg
xxAvg = xsAvgf(d) #x^2 avg
xyAvg = xyAvgf(d) #xy avg
yAvg = yAvgf(d) #y avg

#xxxAvg=xAvg*xsAvg #x^3 avg
xxxAvg=xxxAvgf(d)

xxxxAvg=xxxxAvgf(d)
xxyAvg=xxyAvgf(d)
#y=Ax^2+Bx+C
#A=((xsAvg*yAvg*xsAvg)-(xAvg*yAvg*xxxAvg))/((xsAvg*xsAvg*xsAvg)-(math.pow(xxxAvg,2)))
#B=((xAvg*yAvg*math.pow(xsAvg,2))-(xsAvg*yAvg*xsAvg*xAvg))/((xsAvg*xsAvg*xsAvg)-(math.pow(xxxAvg,2)))
#C=yAvg-B*xAvg-A*xsAvg
A=((xyAvg-xAvg*yAvg)*(xxxxAvg-xxAvg*xxAvg)-(xxyAvg-xxAvg*yAvg)*(xxxAvg-xAvg*xxAvg))/((xxAvg-xAvg*xAvg)*(xxxxAvg-xxAvg*xxAvg)-(xxxAvg-xAvg*xxAvg)*(xxxAvg-xAvg*xxAvg))
B=((xxyAvg-xxAvg*yAvg)*(xxAvg-xAvg*xAvg)-(xyAvg-xAvg*yAvg)*(xxxAvg-xAvg*xxAvg))/((xxAvg-xAvg*xAvg)*(xxxxAvg-xxAvg*xxAvg)-math.pow(xxxAvg-xAvg*xxAvg,2))
C=yAvg-B*xAvg-A*xxAvg


<<<<<<< HEAD

z = np.arange(-100,100,1)
plt.ylim(-100,100)
plt.xlim(-100,100)
=======
z = np.arange(-10,10,1)
plt.ylim(-20,40)
plt.xlim(-20,40)
>>>>>>> ef2f4e737d83fa9d410352deb6e548184d4b74c0
ax = plt.plot(d,'go') #'Go' displays the datapointsax = plt.plot(z,C*z*z+B*z+A)
ax = plt.plot(z,A*z*z+B*z+C)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Regression')
plt.show()
