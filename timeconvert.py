import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import dates as mdates
import math
from datetime import datetime as dt

for BB_index in range(1):
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-DA59'
    XYC = np.imag(np.load(prefix+'.XYC.npy'))
    Y= XYC[0,0:840]
    TS = np.load(prefix+'.TS.npy')
    def time_convert(mytime,myunit='s'):
        if type(mytime).__name__ <>'list': mytime=TS
        myTimestr = [] 
        for time in mytime:
           q1=qa.quantity(time,myunit)
           time1=qa.time(q1,form='ymd')
           myTimestr.append(time1)
        return myTimestr
    def flatten(nested_list): 
        return [e for inner_list in nested_list for e in inner_list]
    Xlist=(flatten(time_convert(1)))
    Xtime= [dt.strptime(d, '%Y/%m/%d/%H:%M:%S') for d in Xlist]
    X=np.array(Xtime)
    if BB_index == 0:
       plt.plot(X,Y,"ro" ,label=BBlist)
       plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
       plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%-m/%-d %-H:%M"))
    elif BB_index == 1:
       plt.plot(X,Y,"bo" ,label=BBlist)
    elif BB_index == 2:
       plt.plot(X,Y,"go" ,label=BBlist)
    else:
       plt.plot(X,Y,"yo" ,label=BBlist)
plt.title('XYphase stability ')
plt.legend(loc='upper right')
plt.xlabel("time")
plt.ylabel("XY imaginary part")
plt.grid()
plt.show()

