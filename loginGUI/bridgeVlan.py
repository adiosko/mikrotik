import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from bridge.bridgeVlan import  bridgeVlan
from loginGUI.addVLAN import addVLANGui

qtCreatorFile = "./loginGUI/vlan.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class bridgeVLAN(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = bridgeVlan(self.server,self.user,self.pwd)
        self.listVlan()

    def listVlan(self):
        devices = self.addr.listVlan()
        self.bridgeField.clear()
        self.vlanField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.bridgeField.addItem( devices[i]['bridge'])
            self.vlanField.addItem(devices[i]['vlan-ids'])
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['bridge']] = devices[i]['.id']

    def enableVlan(self):
        try:
            current = self.bridgeField.currentRow()
            itemName = self.bridgeField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableVlan( str( idName ) )
            self.listVlan()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableVlan(self):
        try:
            current = self.bridgeField.currentRow()
            itemName = self.bridgeField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableVlan( str( idName ) )
            self.listVlan()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def removeVlan(self):
        try:
            current = self.bridgeField.currentRow()
            itemName = self.bridgeField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeVlan( str( idName ) )
            self.listVlan()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Bridge error" )
            self.msg.setInformativeText( str(e)  )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addVlan(self):
        self.nd = addVLANGui(self.user, self.pwd, self.server,self)
        self.nd.show()


    def init_buttons(self):
        self.addButton.clicked.connect( self.addVlan )
        self.enableButton.clicked.connect( self.enableVlan )
        self.disableButton.clicked.connect( self.disableVlan )
        self.removeButton.clicked.connect( self.removeVlan )
        self.refreshButton.clicked.connect( self.listVlan )


