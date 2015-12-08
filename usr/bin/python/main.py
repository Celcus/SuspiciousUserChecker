import os
from sys import platform as _platform

#ActivityMonitor is located in ~/Library/Applications/Utilities/Activity Monitor.app

updateFreq = 5 #can be edited depending on the time set on ActivtyMonitor's update frequency
allowedUsers = ["root", "[adminName]", "_securityagent", "_appleevents", 
                "_spotlight", "_usbmxd", "_dock", "_launchd", "_networkd", 
                "_mdnsresponder", "_windowserver", "_softwareupdate", 
                "_locationd", "_coreaudiod", "_netbios", "_cvmsroot"] #Users/SystemUsers/Daemons allowed and not to be logged by the SUC program

def logNonUser():
  open('log.txt',  w) #will create a logFile if one does not already exist
  
  for theUser in allowedUsers:
    if user != allowedUsers[theUser]:
      write('log.txt', user)
  sleep(updateFreq) #Script waits X seconds before updating again

if _platform == "darwin": #Darwin = OSX
  logNonUser()
else:
  print "This program will probably not run for your OS..."
  sleep(10) #Wait 10seconds before the program quits
  sys.exit(1)
