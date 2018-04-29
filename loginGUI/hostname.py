import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from System.Identity import Identity

qtCreatorFile = "hostname.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class hostnameGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = Identity(self.server,self.user,self.pwd)

    def okButon(self):
        hostname = self.hostnameField.toPlainText()
        self.addr.setHostname(hostname)

    def cancelButon(self):
        sys.exit()

    def init_buttons(self):
        self.cancelButton.clicked.connect( self.cancelButon )
        self.okButton.clicked.connect( self.okButon )