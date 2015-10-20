__author__ = 'Brett A. Hansen'

#Import necessary libs
import subprocess
import os.path

#Check enviorment for all necessary programs
if os.path.isfile('LaunchKioskIR.py') == False:
    print ('No file found')

#Ask for Kiosk SN
KioskSN = raw_input("Enter Kiosk SN: ")

#Open Log File
IRLog = open(KioskSN+'_KioskIR.log','w')

#Capture open connections
subprocess.call('netstat -ano > netstat_'+KioskSN+'.txt', shell=True)
IRLog.write("List open connections: Success\n")

#Capture listening ports
subprocess.call('netstat -fport > fport_'+KioskSN+'.txt', shell=True)
IRLog.write("List listening ports: Success\n")

#Capture all running processes
subprocess.call('tasklist > processlist_'+KioskSN+'.txt', shell=True)
IRLog.write("Process List: Success\n")


#Capture all network connections





IRLog.close()