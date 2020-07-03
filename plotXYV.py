SCR_DIR = '/Users/etohyuki/Desktop/XYPhaseRecalibratedData/ALMA_SV/'
wd = './'
AntenaNumber='DA59'
for BB_index in range(4):
    BBlist = 'BB' + `BB_index + 1`
    prefix = BBlist + '-SPW0-'+AntenaNumber  #PutTheFileName
    timeFile = prefix+'.TS.npy'
    xycFile  = prefix+'.XYC.npy'
    xyvFile  = prefix+'.XYV.npy'
    xypFile  = prefix+'.XYPH.npy'
    azelFile = prefix+'.Azel.npy'
    execfile(SCR_DIR + 'plotXYC.py')
