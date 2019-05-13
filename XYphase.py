import numpy as np
import matplotlib.pyplot as plt
import math

for BB_index in range(4):
    prefix = 'BB' + `BB_index + 1`

    XYCcom = np.load(prefix+'-SPW0-DA59.XYC.npy')
    XYC = np.imag(XYCcom)
    Y= XYC[0,0:840]
    X = np.load(prefix+'-SPW0-DA59.TS.npy')/86400 #sec(MJD)->day(MJD)

    #MJD->#Gregori
    n=X+678881
    a=4*n+3+4*(3/4*(4*(n+1)/(146097)+1))
    b=5*(a%1461)/4+2
    y=a/1461
    m=b/153+3
    d=(b%153)/5
    #print(y,m,d)

    plt.title('XYphase stability',)
    plt.plot(d,Y,"ro" ,label=prefix)
    plt.legend(loc='upper right')
    plt.xlabel("time")
    plt.ylabel("XY img")
    plt.grid()
    plt.show()
