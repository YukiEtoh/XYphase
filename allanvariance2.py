#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt


time = np.load('BB1-SPW0-DA59.TS.npy')
XYphase = np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))[0,0:840]

def w(x):
    deltaT1=np.round(time[x+1]-time[x])
    deltaT2=np.round(time[x+2]-time[x+1])
    if deltaT1 and deltaT2 == 2 :
       return 1
    else:
       return 0
def AllanVar(t):
    y1=XYphase[t]
    y2=XYphase[t+1]
    y3=XYphase[t+2]
    return (y1-2*y2+y3)**2/2*2


def graph():
    X=time[i]-time[0]
    Y=AllanVar(i)
    plt.loglog(X,Y,"ro",markersize=3)
   # b=AllanVar(XYC, 1)
   # a=np.array([  1,   10,  100, 1000],dtype=float)
   # plt.loglog(a,a**(-2)*b,'k')

for i in range(1,838):  #始点の決定
      if w(i)== 1:
         AllanVar(i)
         print(i,time[i]-time[0],AllanVar(i))
         graph()
      else:
        pass 
