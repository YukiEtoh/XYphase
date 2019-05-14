import numpy as np
import matplotlib.pyplot as plt
import math

for BB_index in range(4):
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-DA59'
    XYC = np.imag(np.load(prefix+'.XYC.npy'))
    Y= XYC[0,0:840]
    X = np.load(prefix+'.TS.npy')
def time_convert(mytime,myunit='s'):
    if type(mytime).__name__ <>'list': mytime=X
    myTimestr = [] 
    for time in mytime:
        q1=qa.quantity(time,myunit)
        time1=qa.time(q1,form='dmy')
        myTimestr.append(time1)
    return myTimestr

def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]

P=(flatten(time_convert(1)))
