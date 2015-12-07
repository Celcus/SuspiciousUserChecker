import os
from sys import platform as _platform

#ActivityMonitor is located in ~/Library/Applications/Utilities/Activity Monitor.app

allowedUsers = ["root", "[adminName]", "_securityagent", "_appleevents", 
                "_spotlight", "_usbmxd", "_dock", "_launchd", "_networkd", 
                "_mdnsresponder", "_windowserver", "_softwareupdate", 
                "_locationd", "_coreaudiod", "_netbios", "_cvmsroot"] #Users/SystemUsers/Daemons allowed and not to be logged by the SUC program

def logNonUser():
  open('log.txt',  w) #will create a logFile if one does not already exist
  
  for theUser in allowedUsers:
    if user != allowedUsers[theUser]:
      write('log.txt', user)

if _platform == "darwin": #Darwin = OSX
  logNonUser()
else:
  print "This program will probably not run for your OS..."
