#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import glob
SessionList=['Xb24884_X94f','Xb88fca_X10091','Xb7189f_Xa9cb','Xb8c0d3_X1053','Xb87877_X23c0','Xb945f7_X2f40','Xb903d6_X24ff','Xc20718_X3af7','Xc7111c_X8795','Xb9dfa4_X566e']
BaseBand='BB3'
Band='Band3'
direc='/Users/etohyuki/Desktop/XYPhaseRecalibratedData/'+Band+'/'
def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #return consecutive threepoints
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint
def threePointVar(timeIndex, measuredValue):  #calculate three points
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2
def allanvarhist(allanVar,Frequency):
    plt.hist(allanVar,color='g')
    plt.savefig('HistAllanvarScanBand3'+'.png')
    plt.xlabel("AllanVariance_\sigma^2")
    plt.ylabel("Frequency_TotalData")
    plt.close()
allanvarianceList, timeIntervalList = [], []
for Session in range(1,len(SessionList)):
    files=direc+SessionList[Session]+"/NPY/"
    timeStamp=np.load(glob.glob(files+BaseBand+'*'+'D'+'*TS.npy')[0])
    scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
    dataSize=len(timeStamp)
    XYimagPart=np.imag(np.load(glob.glob(files+BaseBand+'*'+'D'+'*XYC.npy')[0]))[0,0:dataSize]
    TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])
    scangapPoint=np.array([0])
    for ST in range(1,dataSize):   #GetScanTimeInterval
        T=timeStamp[ST]-timeStamp[ST-1]
        if T>3:
           scangapPoint=np.append(scangapPoint,ST)
    for TI in range(1,scangapPoint[1]):  #decide time interval
              Total=0
              num_threePointVariance=0
              for SP in range(1,scangapPoint[1]-2): #decide first point
                  FirstPoint, SecondPoint, ThirdPoint = allanvar_conversion_counter(SP, TI, scaledTime)
                  if SecondPoint and ThirdPoint: 
                     timeIndex_list = [FirstPoint, SecondPoint, ThirdPoint]
                     Total+=threePointVar(timeIndex_list, XYimagPart)
                     num_threePointVariance+=1
              if num_threePointVariance > 0:
                 allanvariance=(Total/num_threePointVariance/TI**2)/2
                 allanvarianceList = allanvarianceList + [allanvariance]
                 timeIntervalList = timeIntervalList + [TI]
allanvarhist(np.log10(allanvarianceList),len(SessionList))


"""
#FIND AVERAGE SCAN INTERVAL TIME
GapTimeTotal=0
TotalCount=0
for Session in range(1,len(SessionList)):
    files=direc+SessionList[Session]+"/NPY/"
    timeStamp=np.load(glob.glob(files+BaseBand+'*'+'D'+'*TS.npy')[0])
    scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
    dataSize=len(timeStamp)
    XYimagPart=np.imag(np.load(glob.glob(files+BaseBand+'*'+'D'+'*XYC.npy')[0]))[0,0:dataSize]
    TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])
    scangapPoint=np.array([0])
    TIME=0
    for ST in range(1,dataSize):   #GetScanTimeInterval
        T=timeStamp[ST]-timeStamp[ST-1]
        if T>3:
           TIME=TIME+np.sum(T)
           scangapPoint=np.append(scangapPoint,ST)
    TotalCount=TotalCount+len(scangapPoint)
    GapTimeTotal=GapTimeTotal+TIME
averageGap=GapTimeTotal/TotalCount
print(averageGap)
""""
