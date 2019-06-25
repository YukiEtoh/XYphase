#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import matplotlib.ticker
fig = plt.figure()
ax = fig.add_subplot(111)
XYC = np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))
x= XYC[0,0:840]
def AllanVar(x, lag):
    vecSize = len(x);       diffSize = vecSize - lag;       avSize = diffSize - lag
    temp = x[lag:vecSize] - x[0:diffSize]
    temp2= temp[lag:diffSize] - temp[0:avSize]
    return np.dot(temp2, temp2) / (2* avSize* lag* lag) #InnerProduct
a=np.linspace(0,3,4)
b=log10(AllanVar(x, 1))
def plot():
    xminors=math.log10(lag)
    yminors=math.log10(AllanVar(x,lag))
    plt.plot(xminors,yminors,"ro",markersize=3)
for lag in range(1,119):
    plot()
for lag in range(121,239):
    plot()
for lag in range(241,359):
    plot()
for lag in range(361,420):
    plot()

    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
    ax.set_xticklabels([0, 3, 10, 32, 100, 316, 1000])
    ax.set_yticklabels([0.0000002, 0.0000004, 0.0000006, 0.0000008, 0.0000010, 0.0000012, 0.0000014, 0.0000016])
    plt.plot(a,-2*a+b,'k')



"""
 np.where(np.diff(TS) > 3.0)[0]
"""
