from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import shutil
import analysisUtils as au
import csv

SCR_DIR = '/Users/etohyuki/Desktop/XYphase'
os.chdir(SCR_DIR)


f = open("PolSessions.txt")
reader = csv.reader(f, delimiter=",", skipinitialspace=True)
data = [ e for e in reader ]


for PL in range(1,2): 
    projectname = data[PL][1]  #プロジェクト名
    objectname = data[PL][2]   #天体名
    EBlist = data[PL][3:7]   #EBリスト　
    session_file = [session[11:18] for session in EBlist]
   # au.asdmExport(EBlist)
    for i in session_file:
        path = SCR_DIR+'/'+objectname+'/'+i
        if not os.path.exists(path):
               os.makedirs(path)
               reEB=EBlist.replace('/', '_') 
               for file in reEB
                   os.renames(file,path)
    

    
    
    




