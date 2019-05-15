import numpy as np
import matplotlib.pyplot as plt
import math

for BB_index in range(4):
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-DA59'
    XYCcom = np.load(prefix+'.XYC.npy')
    XYC = np.imag(XYCcom)
    Y= XYC[0,0:840]
    pi=math.pi
    exp=np.exp
    s2=np.var(Y)
    s=np.std(Y)
    ave=np.average(Y)
    f=(1/np.sqrt(2*pi*s2))*(np.exp(-np.square(Y-ave)/2*s2))

    plt.title('Gaussian distribution',)
    plt.plot(Y,f,"ro" ,label=BBlist)
    plt.legend(loc='upper right')
    plt.xlabel("XY imaginary part")
    plt.ylabel("probability density")
    plt.grid()
    plt.show()
