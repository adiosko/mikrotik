import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from IPv4.Addresses import  Addresses

qtCreatorFile = "ipAddresses.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ipAddressesGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = Addresses(self.server,self.user,self.pwd)
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listAddresses()
        self.ipAddressValues.clear()
        self.networkValues.clear()
        self.interfaceValues.clear()
        for i in devices:
            self.ipAddressValues.addItem( devices[i]['address'])
            self.networkValues.addItem(devices[i]['network'])
            self.interfaceValues.addItem(devices[i]['interface'])

    def addAddress(self):
        self.nd = addAddressGui(self.user,self.pwd,self.server, self)
        self.nd.show()


    def enableAddress(self):
        current = self.ipAddressValues.currentRow()
        itemAddress = self.ipAddressValues.item( current )
        itemNetwork = self.networkValues.item( current )
        itemInterface = self.interfaceValues.item( current )
        self.addr.enableAddress(str(current))
        itemAddress.setFlags( Qt.ItemIsSelectable )
        itemNetwork.setFlags( Qt.ItemIsSelectable)
        itemInterface.setFlags( Qt.ItemIsSelectable)

    def disableAddress(self):
        current = self.ipAddressValues.currentRow()
        itemAddress = self.ipAddressValues.item(current)
        itemNetwork = self.networkValues.item(current)
        itemInterface = self.interfaceValues.item(current)
        self.addr.disableAddress( str(current))
        itemAddress.setFlags(Qt.NoItemFlags)
        itemNetwork.setFlags( Qt.NoItemFlags )
        itemInterface.setFlags( Qt.NoItemFlags )

    def removeAddress(self):
        current = self.ipAddressValues.currentRow()
        self.addr.removeAddress(str(current))
        self.listAddresses()

    # funguje na 30 percent
    def setAddress(self):
        current = self.ipAddressValues.currentRow()
        itemAddress = self.ipAddressValues.item( current)
        self.addr.setAddress( str( current),itemAddress)
        itemAddress.setFlags(Qt.ItemIsEditable)
        self.listAddresses()

    # funguje na 30 percent
    def setNetwork(self):
        current = self.networkValues.currentRow()
        itemNetwork = self.networkValues.item( current )
        self.addr.setNetwork( str( current ),itemNetwork )
        itemNetwork.setFlags( Qt.ItemIsEditable )
        self.listAddresses()

    #funguje na 30 percent
    def setInterface(self):
        current = self.interfaceValues.currentRow()
        itemInterface = self.interfaceValues.item( current )
        itemInterfaceSet = self.interfaceValues.toPlainText()
        itemInterface.setFlags( Qt.ItemIsEditable )
        self.addr.setNetwork( str( current ), itemInterfaceSet )
        self.listAddresses()


    def init_buttons(self):
        self.addButton.clicked.connect( self.addAddress )
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
