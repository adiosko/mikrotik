import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.FirewallAddressist import FirewallAddressList
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "addresslist.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addresslistGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = FirewallAddressList(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listAddressList()
        self.nameField.clear()
        self.addressField.clear()
        self.timeField.clear()
        self.createField.clear()
        self.address_to_id = {}
        for i in devices:
            statetime = ""
            stateCreate = ""
            self.nameField.addItem( devices[i]['list'] )
            self.addressField.addItem(devices[i]['address'])
            try:
                statetime = devices[i]['timeout']
            except:
                statetime = "None"
            self.timeField.addItem( statetime)
            try:
                stateCreate = devices[i]['creation-time']
            except:
                stateCreate = "Unknown"
            self.createField.addItem( stateCreate)
            self.address_to_id[devices[i]['list']] = devices[i]['.id']

    def enableItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableList( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Enable item error" )
            self.msg.setInformativeText( "Cannot enable item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableList( str( idName) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Disable error" )
            self.msg.setInformativeText( "Cannot disable item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeList( str( idName) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Item erro" )
            self.msg.setInformativeText( "Cannot remove item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addItem(self):
        self.nd = addAddressListGui(self.user, self.pwd, self.server,self)
        self.nd.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses )
        self.addButton.clicked.connect(self.addItem)
        self.removeButton.clicked.connect(self.removeItem)
        self.enableButton.clicked.connect(self.enableItem)
        self.disableButton.clicked.connect(self.disableItem)