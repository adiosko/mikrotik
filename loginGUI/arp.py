import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from IPv4.Arp import  Arp
from loginGUI.addArpGui import addArpGui

qtCreatorFile = "arp.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class arpGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = Arp(self.server,self.user,self.pwd)
        self.listArp()

    def listArp(self):
        devices = self.addr.listArp()
        self.ipAddressValues.clear()
        self.macValues.clear()
        self.interfaceValues.clear()
        for i in devices:
            self.ipAddressValues.addItem( devices[i]['address'])
            self.macValues.addItem(devices[i]['mac-address'])
            self.interfaceValues.addItem(devices[i]['interface'])

    def addArp(self):
        self.nd = addArpGui(self.user, self.pwd, self.server,self)
        self.nd.show()

    def enableArp(self):
        current = self.ipAddressValues.currentRow()
        itemAddress = self.ipAddressValues.item( current )
        itemMac = self.macValues.item( current )
        itemInterface = self.interfaceValues.item( current )
        self.addr.enableArp(str(current))
        itemAddress.setFlags( Qt.ItemIsSelectable )
        itemMac.setFlags( Qt.ItemIsSelectable)
        itemInterface.setFlags( Qt.ItemIsSelectable)

    def disableArp(self):
        current = self.ipAddressValues.currentRow()
        itemAddress = self.ipAddressValues.item(current)
        itemMac = self.macValues.item(current)
        itemInterface = self.interfaceValues.item(current)
        self.addr.disableArp( str(current))
        itemAddress.setFlags(Qt.NoItemFlags)
        itemMac.setFlags( Qt.NoItemFlags )
        itemInterface.setFlags( Qt.NoItemFlags )

    def removeArp(self):
        current = self.ipAddressValues.currentRow()
        self.addr.removeArp(str(current))
        self.listArp()

    def init_buttons(self):
        print("text")
        self.addButton.clicked.connect( self.addArp )
        self.enableButton.clicked.connect( self.enableArp )
        self.disableButton.clicked.connect( self.disableArp )
        self.removeButton.clicked.connect( self.removeArp )
        self.refreshButton.clicked.connect( self.listArp )


