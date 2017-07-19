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

dataNum = 3
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. 3=# of points * 3     

xAvg = xAvg(d) #x avg
xsAvg = xsAvg(d) #x^2 avg
xyAvg = xyAvg(d) #xy avg
yAvg = yAvg(d) #y avg
xxxAvg=xAvg*xsAvg #x^3 avg
#y=Ax^2+Bx+C
A=((xsAvg*yAvg*xsAvg)-(xAvg*yAvg*xxxAvg))/((xsAvg*xsAvg*xsAvg)-(math.pow(xxxAvg,2)))
B=((xAvg*yAvg*math.pow(xsAvg,2))-(xsAvg*yAvg*xsAvg*xAvg))/((xsAvg*xsAvg*xsAvg)-(math.pow(xxxAvg,2)))
C=yAvg-B*xAvg-A*xsAvg


z = np.arange(-10,10,1)
plt.ylim(-20,40)
plt.xlim(-20,40)
ax = plt.plot(d,'go') #'Go' displays the datapointsax = plt.plot(z,C*z*z+B*z+A)
ax = plt.plot(z,A*z*z+B*z+C)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Regression')
plt.show()
