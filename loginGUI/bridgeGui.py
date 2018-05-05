import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.BridgeGeneral import  BridgeGeneral
from loginGUI.addBridge import addBridgeGui

qtCreatorFile = "bridge.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class bridgeGUI(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = BridgeGeneral(self.server,self.user,self.pwd)
        self.listBridge()

    def listBridge(self):
        devices = self.addr.listBridge()
        self.nameField.clear()
        self.mtuField.clear()
        self.protocolField.clear()
        self.macField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem( devices[i]['name'])
            self.mtuField.addItem(devices[i]['l2mtu'])
            self.protocolField.addItem(devices[i]['protocol-mode'])
            self.macField.addItem(devices[i]['mac-address'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableBridge(self):
        current = self.nameField.currentRow()
        self.addr.enableBridge( str( current ) )
        self.listBridge()

    def disableBridge(self):
        current = self.nameField.currentRow()
        self.addr.disableBridge( str( current ) )
        self.listBridge()

    def removeBridge(self):
        current = self.nameField.currentRow()
        self.addr.removeBridge( str( current ) )
        self.listBridge()

    def addBridge(self):
        self.nd = addBridgeGui(self.user, self.pwd, self.server,self)
        self.nd.show()

    def init_buttons(self):
        #self.addButton.clicked.connect( self.addVlan )
        self.enableButton.clicked.connect( self.enableBridge )
        self.disableButton.clicked.connect( self.disableBridge )
        self.removeButton.clicked.connect( self.removeBridge )
        self.refreshButton.clicked.connect( self.listBridge )
        self.addButton.clicked.connect(self.addBridge)