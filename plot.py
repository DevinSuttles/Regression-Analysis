
import numpy as np
import matplotlib.pyplot as plt


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

def xyAvg(d):#assumes that x increments as an integer
    sum = 0.0
    counter = 0
    for i in d:
        sum += i*counter
        counter += 1;
    return sum/d.size

def xAvg(d):#assumes that x increments as an integer
    sum = 0.0;
    for i in d:
        sum += 1;
    return sum/d.size

def xsAvg(d):#x squared avg, assumes that x increments as an integer
    sum = 0.0
    counter  = 0
    for i in d:
        sum += counter*counter;
        counter += 1;
    return sum/d.size

def yAvg(d):
    sum = 0.0
    for i in d:
        sum += i
    return sum/d.size

fig1 = plt.figure()

dataNum = 2
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. Right parameter = how many points per x value

xAvg = xAvg(d) #x avg
xsAvg = xsAvg(d) #x^2 avg
xyAvg = xyAvg(d) #xy avg
yAvg = yAvg(d) #yAvg
slope = (xAvg*yAvg-xyAvg)/(xAvg*xAvg-xsAvg)

print(d)
print("x average: ", xAvg, "\nx-squared average: ", xsAvg, "\nxy average: ", xyAvg, "\ny average: ", yAvg)
print("slope =",slope)




yIntercept = yAvg-slope*xAvg
z = np.arange(-10,100,1)
y = slope*z+yIntercept
ax = plt.plot(d,'go') #'Go' displays the datapoints
ax = plt.plot(y,z)
plt.xlim(-1, 10)
plt.ylim(-5,10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Test')

plt.show()