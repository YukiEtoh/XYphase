#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt

def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #return consecutive threepoints
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint
def threePointVar(timeIndex, measuredValue):  #calculate three points
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2
def allanvar_graph(arranVar,timeInterval): #plot the graph
    if BB_index == 0:
       plt.loglog(timeInterval,arranVar,"ro",markersize=3)
    elif BB_index == 0:
       plt.loglog(timeInterval,arranVar,"bo",markersize=3)
    elif BB_index == 0:
       plt.loglog(timeInterval,arranVar,"go",markersize=3)
    else:
       plt.loglog(timeInterval,arranVar,"yo",markersize=3)
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")
    a=np.array([  1,   10,  100, 1000, 10000],dtype=float)
    b=arranVar[0]
    plt.loglog(a,a**(-2)*b,'k')
    plt.savefig('allanvariance_'+BBlist+'.png')
    plt.close()

for BB_index in range(4):   #PutTheNumberOfBaseband
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist +'-'+'SPW0-DA59'  #PutTheFileName
    timeStamp=np.load(prefix+'.TS.npy')
    scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
    dataSize=len(timeStamp)
    XYimagPart=np.imag(np.load(prefix+'.XYC.npy'))[0,0:dataSize]
    TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])
    allanvarianceList, timeIntervalList = [], []

    for TI in range(1,TotalScanTime):  #decide time interval
              Total=0
              num_threePointVariance=0
              for SP in range(1,dataSize-2): #decide first point
                  FirstPoint, SecondPoint, ThirdPoint = allanvar_conversion_counter(SP, TI, scaledTime)
                  if SecondPoint and ThirdPoint: 
                     timeIndex_list = [FirstPoint, SecondPoint, ThirdPoint]
                     Total+=threePointVar(timeIndex_list, XYimagPart)
                     num_threePointVariance+=1
              if num_threePointVariance > 0:
                 allanvariance=(Total/num_threePointVariance/TI**2)/2
                 allanvarianceList = allanvarianceList + [allanvariance]
                 timeIntervalList = timeIntervalList + [TI]
    allanvar_graph(np.array(allanvarianceList), np.array(timeIntervalList))

