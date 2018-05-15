import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DhcpServer import DhcpServer
from loginGUI.addDhcpServer import addDhcpServerGui
#my designed file


qtCreatorFile = "./loginGUI/dhcpserver.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dhcpServerGui(QtGui.QMainWindow,Ui_MainWindow):
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
        devices = self.addr.listDhcp()
        self.nameField.clear()
        self.interfaceField.clear()
        self.leaseField.clear()
        self.poolField.clear()
        self.dynamicField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            statelocal = ""
            statedynamic = ""
            self.nameField.addItem(devices[i]['name'])
            self.interfaceField.addItem(devices[i]['interface'])
            self.leaseField.addItem(devices[i]['lease-time'])
            try:
                statelocal = devices[i]['address-pool']
            except:
                statelocal = "None"
            self.poolField.addItem(statelocal)
            try:
                statedynamic = devices[i]['dynamic']
            except:
                statedynamic = "Static"
            self.dynamicField.addItem(statedynamic)
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableAddress(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableDhcp( str( idName ) )
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
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableDhcp( str( idName ) )
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
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeDhcp( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Dynamic item  error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def addClient(self):
        #self.nd = addDhcpServerGui(self.user, self.pwd, self.server,self)
        #self.nd.show()
        action = addDhcpServerGui( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.setFixedSize(426,229)
        action.show()
        #self.mdi.cascadeSubWindows()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses)
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
        self.addButton.clicked.connect(self.addClient)
        #self.staticButton.clicked.connect(self.makeStatic)