import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.BridgePorts import  BridgePorts
#from loginGUI.addVLAN import addVLANGui

qtCreatorFile = "ports.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class bridgePort(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = BridgePorts(self.server,self.user,self.pwd)
        self.listPorts()

    def listPorts(self):
        devices = self.addr.listPort()
        self.interfaceField.clear()
        self.bridgeField.clear()
        self.priorityField.clear()
        self.costField.clear()
        self.address_to_id = {}
        for i in devices:
            self.interfaceField.addItem( devices[i]['interface'])
            self.bridgeField.addItem(devices[i]['bridge'])
            self.priorityField.addItem(devices[i]['priority'])
            self.costField.addItem(devices[i]['internal-path-cost'])
            self.address_to_id[devices[i]['bridge']] = devices[i]['.id']

    def init_buttons(self):
        #self.addButton.clicked.connect( self.addVlan )
        #self.enableButton.clicked.connect( self.enableVlan )
        #self.disableButton.clicked.connect( self.disableVlan )
        #self.removeButton.clicked.connect( self.removeVlan )
        self.refreshButton.clicked.connect( self.listPorts )