import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from bridge.BridgeHosts import BridgeHosts
#my designed file


qtCreatorFile = "bridgeConnections.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class bridgeConnections(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = BridgeHosts(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listHosts()

    def listHosts(self):
        devices = self.addr.listHosts()
        self.macField.clear()
        self.interfaceField.clear()
        self.ageField.clear()
        self.bridgeField.clear()
        for i in devices:
            self.macField.addItem( devices[i]['mac-address'] )
            self.interfaceField.addItem(devices[i]['on-interface'])
            self.ageField.addItem(devices[i]['age'])
            self.bridgeField.addItem( devices[i]['bridge'] )

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listHosts )