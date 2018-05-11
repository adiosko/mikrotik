import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DhcpServer import DhcpServer
from loginGUI.addSaticDhcpLease import addStaticLease
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "./loginGUI/dhcplease.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dhcpleaseGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DhcpServer(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listLeases()
        self.addressField.clear()
        self.macField.clear()
        self.serverField.clear()
        self.hostField.clear()
        self.statusField.clear()
        self.dynamicField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            stateaddress = ""
            stateserver = ""
            statestatus = ""
            statehost = ""
            try:
                stateaddress = devices[i]['address']
            except:
                stateaddress = "Unassigned"
            self.addressField.addItem(stateaddress)
            self.macField.addItem(devices[i]['mac-address'])
            try:
                stateserver = devices[i]['server']
            except:
                stateserver = "Unknown"
            self.serverField.addItem( stateserver)
            try:
                statehost = devices[i]['host-name']
            except:
                statehost = "Unknown"
            self.hostField.addItem( statehost)
            self.statusField.addItem(devices[i]['status'])
            try:
                devices[i]['dynamic']
                statestatus = "dynamic"
            except:
                statestatus = "static"
            self.dynamicField.addItem(statestatus)
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['address']] = devices[i]['.id']

    def enableLease(self):
        try:
            current = self.addressField.currentRow()
            itemName = self.addressField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableLease( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( "Cannot enable dynamic item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableLease(self):
        try:
            current = self.addressField.currentRow()
            itemName = self.addressField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableLease( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( "Cannot disable dynamic item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeLease(self):
        try:
            current = self.addressField.currentRow()
            itemName = self.addressField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeLease( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Lease item  error" )
            self.msg.setInformativeText( "Cannot remove item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addLease(self):
        self.nd = addStaticLease(self.user, self.pwd, self.server,self)
        self.nd.show()

    def makeStatic(self):
        try:
            current = self.addressField.currentRow()
            itemName = self.addressField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.makeStatic( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Static  error" )
            self.msg.setInformativeText( "Item is already static" )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses)
        self.enableButton.clicked.connect(self.enableLease)
        self.disableButton.clicked.connect(self.disableLease)
        self.removeButton.clicked.connect(self.removeLease)
        self.addButton.clicked.connect(self.addLease)
        self.staticButton.clicked.connect(self.makeStatic)