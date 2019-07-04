#Use in CASA
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.ticker
fig = plt.figure()
ax = fig.add_subplot(111)

for BB_index in range(1):   #PutTheNumberOfBaseband
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-DA59'  #PutTheFileName
    xyc = np.imag(np.load(prefix+'.XYC.npy'))
    XYC= xyc[0,0:840]
    def AllanVar(XYC, lag):
        vecSize = len(XYC);       diffSize = vecSize - lag;       avSize = diffSize - lag
        temp = XYC[lag:vecSize] - XYC[0:diffSize]
        temp2= temp[lag:diffSize] - temp[0:avSize]
        return np.dot(temp2, temp2) / (2* avSize* lag* lag) #InnerProduct
    
 
    def plot():
        X=lag
        Y=AllanVar(XYC,lag)
        plt.loglog(X,Y,"ro",markersize=3)
        b=AllanVar(XYC, 1)
        a=np.array([  1,   10,  100, 1000],dtype=float)
        plt.loglog(a,a**(-2)*b,'k')

    for lag in range(1,118):
        plot()
    for lag in range(121,238):
        plot()
    for lag in range(241,358):
        plot()
    for lag in range(361,420):
        plot()
    plt.title('G31.41+0_a_06_TE/Xb7d0ee BB1')
    plt.xlabel("time lag [s]")
    plt.ylabel("Allan variance")


"""
np.where(np.diff(TS) > 3.0)[0]

"""
