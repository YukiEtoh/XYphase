#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
dataSize=840
scanTime=np.load('BB1-SPW0-DA59.TS.npy')
XYphase=np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))[0,0:dataSize]
scanTimeDiff=np.int(scanTime[dataSize-1]-scanTime[0])
deltaTRange=np.int(scanTime[dataSize-1]-scanTime[0])/2

def allanvar_conversion_counter(startPoint,nextPoint):   #連続した3点を取れたらカウントする関数
    deltaT1=np.int(scanTime[startPoint+nextPoint*1]-scanTime[startPoint])
    deltaT2=np.int(scanTime[startPoint+nextPoint*2]-scanTime[startPoint+nextPoint*1])
    if deltaT1 == deltaT2 :
       return 1
    else:
       return 0
def Total_threePoints(startPoint,nextPoint):  #連続した3点を足し合わせる関数
    vecSize=len(XYphase); y1=XYphase[startPoint]; y2=XYphase[startPoint+nextPoint*1]; y3=XYphase[startPoint+nextPoint*2]
    return (y3-y2-(y2-y1))**2
   
def allanvar_graph(): #グラフをプロット
    X=NP
    Y=N/NP/2
    plt.loglog(X,Y,"ro",markersize=3)
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
   # a=2
   # b=0.0011488759243233671
   # plt.loglog(a,-2+2b+a'k')
print("start point","next point","total of three point")

for NP in range(1,838):  #次点の決定
    N=0
    R=838/NP 
    for SP in range(1,R): #始点の決定
        #print(SP)
        if allanvar_conversion_counter(SP,NP) == 1:
           #print(Total_threePoints(SP,NP))
           N+=Total_threePoints(SP,NP)
           Allanvariance=(N/2)/2
          # print(SP,NP,N)
        else:
           pass
    print(SP,NP,N,N/NP/2)
       # print(SP,NP,N)
       # Allanvariance=(N/2)/2
    allanvar_graph()
