#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import glob
Band='Band3'
SessionList=['Xb24884_X94f','Xb88fca_X10091','Xb7189f_Xa9cb','Xb8c0d3_X1053','Xb87877_X23c0','Xb945f7_X2f40','Xb903d6_X24ff','Xc20718_X3af7','Xc7111c_X8795','Xb9dfa4_X566e']
BaseBand='BB4'
direc='/Users/etohyuki/Desktop/XYPhaseRecalibratedData/'+Band+'/'
TimeRange=[1320]
def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #return consecutive threepoints
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint
def threePointVar(timeIndex, measuredValue):  #calculate three points
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2
def allanvarhist(allanVar,Frequency):
    plt.hist(allanVar)
    plt.savefig('HistAllanvar'+Band+'.png')
    plt.xlabel("AllanVariance[dex]")
    plt.ylabel("Frequency_TotalData")
    plt.close()
def flatten(nested_list): 
    return [e for inner_list in nested_list for e in inner_list]

def getNearestValue(samplevalue, anynumber):
    idx = np.abs(np.asarray(samplevalue) - anynumber).argmin()
    return samplevalue[idx]
any_allan=[]
for Session in range(0,len(SessionList)):
    files=direc+SessionList[Session]+"/NPY/"
    timeStamp=np.load(glob.glob(files+BaseBand+'*'+'D'+'*TS.npy')[0])
    scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
    dataSize=len(timeStamp)
    XYimagPart=np.imag(np.load(glob.glob(files+BaseBand+'*'+'D'+'*XYC.npy')[0]))[0,0:dataSize]
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
    allan_time=[flatten(allanvarianceList),timeIntervalList] #CreatePairOfAllan&Time
#    exec('allan_'+str(Session) + '=[flatten(allanvarianceList),(timeIntervalList)]') #CreatePairOfAllan&Time

    anyAllanIndex=allan_time[1].index(getNearestValue(allan_time[1],TimeRange))
    print(getNearestValue(allan_time[1],TimeRange))
    any_allan.append(allan_time[0][anyAllanIndex])
allanvarhist(any_allan,len(SessionList))
#allanvarhist(np.log10(allanvarianceList),len(SessionList))
#    print(np.array(int(math.log10(allanvarianceList))),Session)
 
