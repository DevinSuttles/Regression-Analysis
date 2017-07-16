
import numpy as np
import matplotlib.pyplot as plt


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

fig1 = plt.figure()

x = 10*np.random.rand(10, 1)#10=x&y limit and # of points. 3=# of points * 3

z = np.arange(0,10,.005)
y = -z+10
ax = plt.plot(x,'go') #'Go' displays the datapoints
ax = plt.plot(y,z)
plt.xlim(-1, 10)
plt.ylim(0,10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Test')

plt.show()