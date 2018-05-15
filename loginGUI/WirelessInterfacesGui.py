import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from wireless.interfaces import interfaces
from loginGUI.addWirelessInterface import addWirelessInterfaceGui
#my designed file


qtCreatorFile = "./loginGUI/wirelessInterface.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class wirelessInterfaceGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = interfaces(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listInterfaces()

    def listInterfaces(self):
        devices = self.addr.listInterfaces()
        self.nameField.clear()
        self.typeField.clear()
        self.linkdownField.clear()
        self.runField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.linkdownField.addItem(devices[i]['link-downs'])
            state = ""
            try:
                state = devices[i]['running']
            except:
                state = "Unknown"
            self.runField.addItem(state)
            statedis = ""
            try:
                statedis = devices[i]['disabled']
            except:
                statedis = "Unknown"
            self.disableField.addItem(statedis)
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def removeInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeInterface( str( current ) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Master interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def enableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableInterface( str( current ) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Master interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def disableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableInterface( str( current ) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Master interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def addInterface(self):
        #self.nd = addWirelessInterfaceGui( self.user, self.pwd, self.server, self )
        #self.nd.show()
        action = addWirelessInterfaceGui( self.user, self.pwd, self.server,self )
        self.parent.mdi.addSubWindow( action )
        action.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.enableButton.clicked.connect(self.enableInterface)
        self.disableButton.clicked.connect(self.disableInterface)
        self.removeButton.clicked.connect(self.removeInterface)
        self.addButton.clicked.connect(self.addInterface)