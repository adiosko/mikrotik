import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.FirewallCOnnections import FirewallConnections
#my designed file


qtCreatorFile = "fwconnection.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class fwConnection(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = FirewallConnections(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listConnections()

    def listConnections(self):
        devices = self.addr.listConnections()
        self.srcField.clear()
        self.dstField.clear()
        self.protField.clear()
        self.tcpstateField.clear()
        self.confirmField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            self.srcField.addItem( devices[i]['src-address'] )
            self.dstField.addItem(devices[i]['dst-address'])
            self.protField.addItem(devices[i]['protocol'])
            try:
                self.tcpstateField.addItem(devices[i]['tcp-state'])
            except:
                state = "Not established"
            try:
                self.confirmField.addItem(devices[i]['confirmed'])
            except:
                state = "Seen reply,Assured,Confirmed"
            self.address_to_id[devices[i]['src-address']] = devices[i]['.id']

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listConnections )