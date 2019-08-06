#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #連続する第1点・2点・3点を返す
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint

def threePointVar(timeIndex, measuredValue):  #連続する3点における計算値を返す
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2

def allanvar_graph(arranVar,timeInterval): #グラフをプロット
    plt.loglog(timeInterval,arranVar,"ro",markersize=3)
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
    a=np.array([  1,   10,  100, 1000, 10000],dtype=float)
    b=arranVar[0]
    plt.loglog(a,a**(-2)*b,'k')

timeStamp=np.load('BB1-SPW0-DA59.TS.npy')
scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
dataSize=len(timeStamp)
XYimagPart=np.imag(np.load('BB1-SPW0-DA59.XYC.npy'))[0,0:dataSize]
TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])
allanvarianceArray=np.array([]);timeIntervalArray=np.array([])
for TI in range(1,TotalScanTime):  #次点の決定
          Total=0
          num_threePointVariance=0
          for SP in range(1,dataSize-2): #始点の決定
              if allanvar_conversion_counter(SP, TI, scaledTime)[1] and allanvar_conversion_counter(SP, TI, scaledTime)[2]:
                 conter=allanvar_conversion_counter(SP, TI, scaledTime)
                 timeIndex_list=np.hstack((conter[0],conter[1],conter[2])).tolist()
                 Total+=threePointVar(timeIndex_list, XYimagPart)
                 num_threePointVariance+=1
          if num_threePointVariance > 1:
             allanvariance=(Total/num_threePointVariance/TI**2)/2
             allanvarianceArray=np.append(allanvarianceArray, allanvariance)
             timeIntervalArray=np.append(timeIntervalArray,TI)
allanvar_graph(allanvarianceArray,timeIntervalArray)

