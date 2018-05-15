import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.BridgePorts import  BridgePorts
from loginGUI.addPort import addPortGui

qtCreatorFile = "./loginGUI/ports.ui"

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
        self.statusField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            status = ""
            self.interfaceField.addItem( devices[i]['interface'])
            try:
                status = devices[i]['bridge']
            except:
                status = "Unknown"
            self.bridgeField.addItem(status)
            self.priorityField.addItem(devices[i]['priority'])
            self.costField.addItem(devices[i]['path-cost'])
            self.statusField.addItem(devices[i]['status'])
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['interface']] = devices[i]['.id']

    def removePort(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removePort( str( idName) )
            self.listPorts()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def enablePort(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enablePort( str( idName) )
            self.listPorts()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disablePort(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disablePort( str( idName) )
            self.listPorts()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def addPort(self):
        action = addPortGui( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()

    def init_buttons(self):
        #self.addButton.clicked.connect( self.addVlan )
        self.enableButton.clicked.connect( self.enablePort)
        self.disableButton.clicked.connect( self.disablePort )
        self.removeButton.clicked.connect( self.removePort)
        self.refreshButton.clicked.connect( self.listPorts )
        self.addButton.clicked.connect(self.addPort)