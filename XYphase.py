import numpy as np
import matplotlib.pyplot as plt
import math


for BB_index in range(4):
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-DA59'
    XYC = np.imag(np.load(prefix+'.XYC.npy'))
    Y= XYC[0,0:840]
    X = np.load(prefix+'.TS.npy')
    if BB_index == 0: 
       plt.plot(X,Y,"ro" ,label=BBlist)
    elif BB_index == 1:
       plt.plot(X,Y,"bo" ,label=BBlist)
    elif BB_index == 2:
       plt.plot(X,Y,"go" ,label=BBlist)
    else:
       plt.plot(X,Y,"yo" ,label=BBlist)
plt.title('XYphase stability')
plt.legend(loc='upper right')
plt.xlabel("time")
plt.ylabel("XY imaginary part")
plt.grid()
plt.show()
