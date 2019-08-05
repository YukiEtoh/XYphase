#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt

timeStamp=np.load('BB1-SPW0-DA59.TS.npy')
scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))  
dataSize=len(timeStamp)
XYphase=np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))[0,0:dataSize]
TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])

def allanvar_conversion_counter(startPoint,timeInterval):   #連続した3点を取れたらカウントする関数
    nextPoint=np.where(np.round(scaledTime[startPoint]+timeInterval)==np.round(scaledTime))[0]
    thirdPoint=np.where(np.round(scaledTime[startPoint]+timeInterval*2)==np.round(scaledTime))[0]
    if nextPoint and thirdPoint :
       return 1
    else:
       return 0

def Total_threePoints(startPoint,timeInterval):  #連続した3点を足し合わせアラン分散を計算する関数
    nextPoint=np.where(np.round(scaledTime[startPoint]+timeInterval)==np.round(scaledTime))[0]
    thirdPoint=np.where(np.round(scaledTime[startPoint]+timeInterval*2)==np.round(scaledTime))[0]
    y1=XYphase[startPoint]; y2=XYphase[int(nextPoint)]; y3=XYphase[int(thirdPoint)]
    threePoints=(y3-2*y2-y1)**2
    return threePoints
    

def allanvar_graph(): #グラフをプロット
    X=TI
    Y=allan
    plt.loglog(X,Y,"ro",markersize=3)
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
    a=np.array([  2,   10,  100, 1000],dtype=float)
    b=5.8e-6
    plt.loglog(a,a**(-2)*b,'k')

for TI in range(1,TotalScanTime):  #次点の決定
          Total=0
          N=0
          for SP in range(1,dataSize-2): #始点の決定
              if allanvar_conversion_counter(SP,TI) == 1:
                 Total+=Total_threePoints(SP,TI)
                 N+=allanvar_conversion_counter(SP,TI)
             #    print(TI,Total,N,SP)
              else:
                 pass
          if not N ==0:
            # print(Total,N)   
             allan=(Total/N/TI**2)/2
             allanvar_graph()
          else:
             pass
    

