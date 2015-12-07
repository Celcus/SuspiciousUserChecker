import os
from sys import platform as _platform

#ActivityMonitor is located in ~/Library/Applications/Activity_Monitor.eze (I think)

allowedUsers = ["root", "[adminName]", "_securityagent", "_appleevents", 
                "_spotlight", "_usbmxd", "_dock", "_launchd"] #Users allowed and not to be logged by the SUC program

def logNonUser():
  open('log.txt',  w) #will create a logFile if one does not already exist

if _platform == "darwin": #Darwin = OSX
  logNonUser()
else:
  print "This program will probably not run for your OS..."
