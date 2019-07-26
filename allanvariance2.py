#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
MJDsec=np.load('BB1-SPW0-DA59.TS.npy')
XYphase=np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))[0,0:840]
scanTotal=np.round(np.sum(MJDsec))
def allanvar_conversion_counter(startPoint,timeDiff):
    deltaT1=np.round(time[startPoint+timeDiff]-time[startPoint])
    deltaT2=np.round(time[startPoint+2*timeDiff]-time[startPoint+timeDiff])
    if deltaT1 and deltaT2 == 2*timeDiff:
       return 1
    else:
       return 0
def N(tau):
    vecSize=len(XYphase); y1=XYphase[i]; y2=XYphase[i+tau]; y3=XYphase[i+2*tau]
    return (y3-y2-(y2-y1))**2

   
def graph():
    X=2*deltaT
    Y=Allanvariance
    plt.loglog(X,Y,"ro",markersize=3)
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
   # a=2
   # b=0.0011488759243233671
   # plt.loglog(a,-2+2b+a'k')


for deltaT in range(1,4183211173150):
    total=0
    NumOfData=datasize/deltaT-2
    for i in range(1,NumOfData):  #始点の決定
        if w(i,deltaT)== 1:
           total+=N(deltaT)
        else:
           pass
    Allanvariance=(total/deltaT)/2
#    print(Allanvariance,deltaT)
    graph()

