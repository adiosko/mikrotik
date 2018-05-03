import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from wireless.interfaces import interfaces
from loginGUI.addWirelessInterface import addWirelessInterfaceGui
#my designed file


qtCreatorFile = "wirelessInterface.ui"

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
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.linkdownField.addItem(devices[i]['link-downs'])

    def removeInterface(self):
        current = self.nameField.currentRow()
        self.addr.removeInterface( str( current ) )
        self.listInterfaces()

    def enableInterface(self):
        current = self.nameField.currentRow()
        self.addr.enableInterface( str( current ) )
        self.listInterfaces()

    def disableInterface(self):
        current = self.nameField.currentRow()
        self.addr.disableInterface( str( current ) )
        self.listInterfaces()

    def addInterface(self):
        self.nd = addWirelessInterfaceGui( self.user, self.pwd, self.server, self )
        self.nd.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.enableButton.clicked.connect(self.enableInterface)
        self.disableButton.clicked.connect(self.disableInterface)
        self.removeButton.clicked.connect(self.removeInterface)
        self.addButton.clicked.connect(self.addInterface)