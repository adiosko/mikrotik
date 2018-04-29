import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from System.ResetConfig import ResetConfig

qtCreatorFile = "reset.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class resetGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = ResetConfig(self.server,self.user,self.pwd)

    def keepUserConfig(self):
        self.addr.keepUser()
        sys.exit()

    def capsMode(self):
        self.addr.capsReset()
        sys.exit()

    def nodefault(self):
        self.addr.noDefault()
        sys.exit()

    def donotBackup(self):
        self.addr.skipbackup()
        sys.exit()

    def init_buttons(self):
        self.keepuserButton.clicked.connect( self.keepUserConfig )
        self.capsButton.clicked.connect( self.capsMode)
        self.nodefaultButton.clicked.connect( self.nodefault )
        self.notbackupButton.clicked.connect(self.donotBackup)