import numpy as np
import matplotlib.pyplot as plt
import math

def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

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

dataNum = 2
d = 10*np.random.rand(dataNum, 1)#10=x&y limit and # of points. 3=# of points * 3

