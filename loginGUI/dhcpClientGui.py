import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DhcpCLient import DhcpClient
from loginGUI.addDhcpClient import addDhcpclientGui
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "./loginGUI/dhcpclient.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dhcpClientGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DhcpClient(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listCLients()
        self.interfaceField.clear()
        self.addressField.clear()
        self.expiresField.clear()
        self.statusField.clear()
        self.dynamicField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            stateaddress = ""
            stateexpires = ""
            statestatus = ""
            statehost = ""
            self.interfaceField.addItem(devices[i]['interface'])
            try:
                stateaddress = devices[i]['address']
            except:
                stateaddress = "Unassigned"
            self.addressField.addItem(stateaddress)
            try:
                stateexpires = devices[i]['expires-after']
            except:
                stateexpires = "Unknown"
            self.expiresField.addItem( stateexpires )
            try:
                statestatus = devices[i]['status']
            except:
                statestatus = "Unknown"
            self.statusField.addItem( statestatus)
            self.dynamicField.addItem( devices[i]['dynamic'] )
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['interface']] = devices[i]['.id']

    def enableAddress(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableAddress( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableAddress(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableAddress( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeAddress(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeAddress( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Lease item  error" )
            self.msg.setInformativeText( str(e))
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def addClient(self):
        #self.nd = addDhcpclientGui(self.user, self.pwd, self.server,self)
        #self.nd.show()
        action = addDhcpclientGui( self.user, self.pwd, self.server, self )
        self.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def releaseAddress(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.releaseAddress( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Release error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def renewAddress(self):
        try:
            current = self.interfaceField.currentRow()
            itemName = self.interfaceField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.releaseAddress( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Renew error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses)
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
        self.releaseButton.clicked.connect(self.releaseAddress)
        self.renewButton.clicked.connect(self.renewAddress)
        self.addButton.clicked.connect(self.addClient)
        #self.staticButton.clicked.connect(self.makeStatic)