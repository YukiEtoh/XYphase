#This script create the histgram of allanvariance-frequency in any timescale

#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import glob
Band='Band6'
SessionList=['Xb7d0ee_X63d5',  'Xc1fe31_X6fa',  'Xc1e2be_X39e9',  'Xad565b_X1ae7',  'Xb47876_X554d', 'Xb47876_Xae6',  'Xb48b38_X1219',  'Xb618c7_X5b22',  'Xb25e1a_X44d',  'Xb25e1a_Xb124',  'Xc079b5_X8b4',  'Xc1f4d6_X676',   'Xba839d_X2096',  'Xbe22c2_X2db0',  'Xbe5932_X1b25']
BaseBand='BB1'
direc='/Users/etohyuki/Desktop/XYPhaseRecalibratedData/'+Band+'/'
TimeRange=2215
def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #return consecutive threepoints
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint
def threePointVar(timeIndex, measuredValue):  #calculate three points
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2
def allanvarhist(allanVar,Frequency):
    plt.hist(allanVar,color='b')
    plt.savefig('HistAllanvar_'+str(TimeRange)+'[s]'+Band+'_'+BaseBand+'.png')
    plt.xlabel("AllanVariance[dex]")
    plt.ylabel("Frequency_TotalData")
    plt.title('HistAllanvar_'+str(TimeRange)+'[s]'+Band+'_'+BaseBand)
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
    allanvarianceList, timeIntervalList ,allan_nomalizedList = [], [], []
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
           allan_nomalized = allanvariance*TI**2
           allanvarianceList = allanvarianceList + [allanvariance]
           timeIntervalList = timeIntervalList + [TI]
           allan_nomalizedList = allan_nomalizedList + [allan_nomalized]
    allan_time=[flatten(allan_nomalizedList),timeIntervalList]
    #allan_time=[flatten(allanvarianceList),timeIntervalList] #CreatePairOfAllan&Time
    #exec('allan_'+str(Session) + '=[flatten(allanvarianceList),(timeIntervalList)]') #CreatePairOfAllan&Time

    anyAllanIndex=allan_time[1].index(getNearestValue(allan_time[1],TimeRange))
    print(getNearestValue(allan_time[1],TimeRange))
    any_allan.append(allan_time[0][anyAllanIndex])
allanvarhist(np.log10(any_allan),len(SessionList))
#allanvarhist(np.log10(allanvarianceList),len(SessionList))
#    print(np.array(int(math.log10(allanvarianceList))),Session)

"""
#FIND ALLAN SESSION TIME
allanvarianceList, timeIntervalList = [], []
for Session in range(0,len(SessionList)):
    files=direc+SessionList[Session]+"/NPY/"
    timeStamp=np.load(glob.glob(files+BaseBand+'*'+'D'+'*TS.npy')[0])
    scaledTime = np.round((timeStamp-np.min(timeStamp))/np.min(np.diff(timeStamp)))
    dataSize=len(timeStamp)
    XYimagPart=np.imag(np.load(glob.glob(files+BaseBand+'*'+'D'+'*XYC.npy')[0]))[0,0:dataSize]
    TotalScanTime=np.int(scaledTime[dataSize-1]-scaledTime[0])
   
    for TI in range(1,TotalScanTime):  #decide time interval
              Total=0
              num_threePointVariance=0
              for SP in range(1,dataSize-2): #decide first point
                  FirstPoint, SecondPoint, ThirdPoint = allanvar_conversion_counter(SP, TI, scaledTime)
                  if SecondPoint and ThirdPoint:

                     Total+=threePointVar(timeIndex_list, XYimagPart)
                     num_threePointVariance+=1
              if num_threePointVariance > 0:
              #   allanvariance=(Total/num_threePointVariance/TI**2)/2

                 timeIntervalList = timeIntervalList + [TI]
    print(timeIntervalList[-1])
"""    

