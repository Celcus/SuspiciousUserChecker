import os
from sys import platform as _platform

#ActivityMonitor is located in ~/Library/Applications/Utilities/Activity Monitor.app

updateFreq = 5 #can be edited depending on the time set on ActivtyMonitor's update frequency
allowedUsersOSX = ["root", "[adminName]", "_securityagent", "_appleevents", 
                "_spotlight", "_usbmxd", "_dock", "_launchd", "_networkd", 
                "_mdnsresponder", "_windowserver", "_softwareupdate", "_locationd", 
                "_coreaudiod", "_netbios", "_cvmsroot", "_netbios"] #Users/SystemUsers/Daemons allowed and ignored by the SUC script

allowedUsersLinux = []

def logNonUserOSX():
  open('log.txt',  w) #will create a logFile if one does not already exist
  
  for theUser in allowedUsersOSX:
    if user != allowedUsersOSX[theUser]:
      write('log.txt', user)
  sleep(updateFreq) #Script waits X seconds before updating again
  
def logNonUserLinux():
  open('log.txt', w)
  for theUser in allowedUsersLinux:
    if user !- allowedUsersLinux[theUser]:
      write('log.txt', user)
    sleep(updateFreq)

if _platform == "darwin": #Darwin = OSX
  logNonUserOSX()
else:
  print "This program will probably not run for your OS..."
  sleep(10) #Wait 10seconds before the program quits
  sys.exit(1)
