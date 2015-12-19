#! usr/bin/python

#Script is to be used for scanning for malicious users in systems running OSX
#Its not complete...

import os
from sys import platform as _platform


#ActivityMonitor is located in ~/Library/Applications/Utilities/Activity Monitor.app
updateFreq = 5 #can be edited depending on the time set on ActivtyMonitor's update frequency
allowedUsersOSX = ["root", "adminName", "_securityagent", "_appleevents", 
                "_spotlight", "_usbmxd", "_dock", "_launchd", "_networkd", 
                "_mdnsresponder", "_windowserver", "_softwareupdate", "_locationd", 
                "_coreaudiod", "_netbios", "_cvmsroot", "_netbios"] #Users or SystemUsers or Daemons ignored by the SUC script

allowedUsersLinux = []

def logNonUserOSX():
    open('log.txt',  w) #will create a logFile if one does not already exist
    
    for line in logFile:
        lineElements = line.split()
        user = lineElements[0]     # find the position of user and replace "0" with the appropriate index
        StartTime = lineElements[1] # get all the information you need in this way
 
        if user not in allowedUsers:
            ToFole.writelines(user + '\t' + StartTime)
            ToFile = open('log.txt',  w) #will create a logFile if one does not already exist
            ToFile.writelines('User\tStartTime\n')   # will write the column names to the log.txt file

    logFile = # give the source of the log file
    sleep(updateFreq) #Script waits X seconds before updating again
try:
  if _platform == "darwin": #Darwin = OSX
    logNonUserOSX()
except os.error:
  print "This program will probably not run for your OS..."
  sleep(10) #Wait 10seconds before the program quits
  sys.exit(1)
