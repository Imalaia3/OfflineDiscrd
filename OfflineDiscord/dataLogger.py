import os
from getdate import *

dt = str(getNowDate())
dt1 = dt.replace(":", "a")
createSecondLogFile = True


def enableCreateSecondLogFile():
    global createSecondLogFile
    createSecondLogFile = True


def disableCreateSecondLogFile():
    global createSecondLogFile
    createSecondLogFile = False



def logData(data):
    if createSecondLogFile == True:
        Lfile = open("Log " + dt1 + ".log", "w")
        print("Data was written in logfile (" + dt1 + ".log)")
        Lfile.write(data)

    else:
        
        fhgdfgh = open("log.log", "w")
        fhgdfgh.write(dt1 + "===> " + data)
        print("Data was written in logfile (log.log)")
