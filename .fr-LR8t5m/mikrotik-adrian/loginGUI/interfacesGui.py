import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.interfaces import interfaces
#my designed file


qtCreatorFile = "./loginGUI/interfaces.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class interfaceGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.disabledField.clear()
        self.runField.clear()
        self.txField.clear()
        self.rxField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            self.nameField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.linkdownField.addItem(devices[i]['link-downs'])
            try:
                state = devices[i]['disabled']
            except:
                state = "Unknown"
            self.disabledField.addItem(state)
            self.runField.addItem(devices[i]['running'])
            self.txField.addItem(devices[i]['tx-byte'])
            self.rxField.addItem(devices[i]['rx-byte'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableInterface( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableInterface( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText(str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.enableButton.clicked.connect(self.enableInterface)
        self.disableButton.clicked.connect(self.disableInterface)
