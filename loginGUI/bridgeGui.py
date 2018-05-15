import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.BridgeGeneral import  BridgeGeneral
from loginGUI.addBridge import addBridgeGui

qtCreatorFile = "./loginGUI/bridge.ui"

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
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem(devices[i]['name'])
            try:
                status = devices[i]['l2mtu']
            except:
                status = "None"
            self.mtuField.addItem(status )
            self.protocolField.addItem(devices[i]['protocol-mode'])
            self.macField.addItem(devices[i]['mac-address'])
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableBridge(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableBridge( str( current ) )
            self.listBridge()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableBridge(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableBridge( str( current ) )
            self.listBridge()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeBridge(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeBridge( str( current ) )
            self.listBridge()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addBridge(self):
        action = addBridgeGui( self.user, self.pwd, self.server, self)
        self.parent.mdi.addSubWindow( action )
        action.setFixedSize(376,103)
        action.show()
        #self.mdi.cascadeSubWindows()

    def init_buttons(self):
        #self.addButton.clicked.connect( self.addVlan )
        self.enableButton.clicked.connect( self.enableBridge )
        self.disableButton.clicked.connect( self.disableBridge )
        self.removeButton.clicked.connect( self.removeBridge )
        self.refreshButton.clicked.connect( self.listBridge )
        self.addButton.clicked.connect(self.addBridge)