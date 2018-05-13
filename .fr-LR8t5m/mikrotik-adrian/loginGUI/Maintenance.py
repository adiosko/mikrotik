import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from System.SystemMaintenance import SystemMaintenance

class Maintenance:
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.addr = SystemMaintenance(server,user,pwd)

    def reboot(self):
        self.addr.rebootRouter()

    def shutdown(self):
        self.addr.shutdownRouter()

