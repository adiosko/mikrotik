import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DhcpRelay import DhcpRelay
from loginGUI.addDhcpRelayGui import addDhcpRelayGui
#my designed file


qtCreatorFile = "dhcprelay.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dhcpRelayGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DhcpRelay(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listRelay()
        self.nameField.clear()
        self.interfaceField.clear()
        self.dhcpField.clear()
        self.localField.clear()
        self.address_to_id = {}
        for i in devices:
            statelocal = ""
            self.nameField.addItem(devices[i]['name'])
            self.interfaceField.addItem(devices[i]['interface'])
            self.dhcpField.addItem(devices[i]['dhcp-server'])
            try:
                statelocal = devices[i]['local-address']
            except:
                statelocal = "None"
            self.localField.addItem(statelocal)
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableAddress(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRelay( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( "Cannot enable dynamic item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableAddress(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRelay( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( "Cannot enable dynamic item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeAddress(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeRelay( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( "Cannot enable dynamic item" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def addClient(self):
        self.nd = addDhcpRelayGui(self.user, self.pwd, self.server,self)
        self.nd.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses)
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
        self.addButton.clicked.connect(self.addClient)
        #self.staticButton.clicked.connect(self.makeStatic)