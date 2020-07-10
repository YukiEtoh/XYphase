#This script create the histgram of variance in one session

#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt
import glob
"""
Band='Band3'
SessionList=['Xb24884_X94f','Xb88fca_X10091','Xb7189f_Xa9cb','Xb8c0d3_X1053','Xb87877_X23c0','Xb945f7_X2f40','Xc20718_X3af7','Xb9dfa4_X566e']
direc='/Users/etohyuki/Desktop/XYPhaseRecalibratedData/'+Band+'/'
"""
Band='Band6'
SessionList=['Xb7d0ee_X63d5',  'Xc1fe31_X6fa',  'Xc1e2be_X39e9',   'Xb47876_X554d', 'Xb47876_Xae6',  'Xb48b38_X1219',  'Xb618c7_X5b22',  'Xb25e1a_X44d',  'Xb25e1a_Xb124',  'Xc079b5_X8b4',  'Xc1f4d6_X676',    'Xba839d_X2096',  'Xbe22c2_X2db0',  'Xbe5932_X1b25']

def variancehist(Variance):
    if Band == 'Band3':
       plt.hist(Variance,color='b',rwidth=1, bins=20)
    if Band == 'Band6':
       plt.hist(Variance,color='g',rwidth=1, bins=50)
    plt.savefig('SessionVariance_allBaseBand'+Band+'.png')
    plt.xlabel('variance')
    plt.ylabel('Frequency')
    plt.close()

SessionVar=[]
for Session in range(0,len(SessionList)):
    files=direc+SessionList[Session]+"/NPY/"
    for BB_index in range(4):
        BBlist = 'BB' + `BB_index + 1`
        timeStamp=np.load(glob.glob(files+BBlist+'*'+'D'+'*TS.npy')[0])
        dataSize=len(timeStamp)
        XYimagPart=np.imag(np.load(glob.glob(files+BBlist+'*'+'D'+'*XYC.npy')[0]))[0,0:dataSize]
        oneSessionBB_var= np.var(XYimagPart[0:len(XYimagPart)+1])
        SessionVar=SessionVar + [oneSessionBB_var]
variancehist(SessionVar)

