import matplotlib.dates as mdates
import os
import shutil
import analysisUtils as au
import csv

SCR_DIR = '/sciopsparking/yetoh/'
os.chdir(SCR_DIR)

f = open("PolSessions.txt")
reader = csv.reader(f, delimiter=",", skipinitialspace=True)
data = [ e for e in reader ]

for PL in range(10,11):
    projectname = data[PL][0]
    objectname = data[PL][1]
    EBlist = data[PL][2:12]
    for session in EBlist:
        EB=session.replace('/', '_').replace(':', '_')
        au.asdmExport(session)
        session_file = session[11:18]
        PATH = SCR_DIR + objectname+'/'+session_file
        if not os.path.exists(PATH):
               os.makedirs(PATH)
               shutil.move(EB,PATH+'/'+EB)
        else:
               shutil.move(EB,PATH+'/'+EB)

