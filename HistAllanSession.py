#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import glob

SessionList=["Xb24884_X94f","Xb88fca_X10091","Xacbbd0_X132c","Xb7189f_Xa9cb","Xb8c0d3_X1053","Xb87877_X23c0","Xb945f7_X2f40","Xb903d6_X24ff","Xc20718_X3af7","Xc7111c_X8795","Xb9dfa4_X566e"]
BaseBand='BB1'
direc='/Users/etohyuki/Desktop/XYPhaseRecalibratedData/'

def allanvar_conversion_counter(startPoint, timeInterval, integerTimeCode):  #return consecutive threepoints
    nextPoint = np.where( integerTimeCode[startPoint] + timeInterval == integerTimeCode)[0]
    thirdPoint = np.where( integerTimeCode[startPoint] + timeInterval*2 == integerTimeCode)[0]
    return np.array([startPoint]), nextPoint, thirdPoint
def threePointVar(timeIndex, measuredValue):  #calculate three points
    return (measuredValue[timeIndex[0]] - 2*measuredValue[timeIndex[1]] + measuredValue[timeIndex[2]])**2
def allanvarhist(allanVar,Frequency):
    plt.hist(allanVar)
    #ax=plt.hist(allanVar, normed=False)
    #ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    plt.savefig('Hist'+'.png')
    
    plt.close()

allanvarianceList, timeIntervalList = [], []
for Session in range(1,2):
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
                     timeIndex_list = [FirstPoint, SecondPoint, ThirdPoint]
                     Total+=threePointVar(timeIndex_list, XYimagPart)
                     num_threePointVariance+=1
              if num_threePointVariance > 0:
                 allanvariance=(Total/num_threePointVariance/TI**2)/2
                 allanvarianceList = allanvarianceList + [allanvariance]
                 timeIntervalList = timeIntervalList + [TI]
allanvarhist(np.log10(allanvarianceList),len(SessionList))
#    print(np.array(int(math.log10(allanvarianceList))),Session)