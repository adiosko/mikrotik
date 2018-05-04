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
        self.dynamicField.clear()
        self.address_to_id = {}
        for i in devices:
            self.ipAddressValues.addItem( devices[i]['address'])
            self.macValues.addItem(devices[i]['mac-address'])
            self.interfaceValues.addItem(devices[i]['interface'])
            self.dynamicField.addItem(devices[i]['dynamic'])
            self.address_to_id[devices[i]['address']] = devices[i]['.id']

    def addArp(self):
        self.nd = addArpGui(self.user, self.pwd, self.server,self)
        self.nd.show()

    def enableArp(self):
        currentAddress = self.ipAddressValues.currentRow()
        currentMac = self.macValues.currentRow()
        currentInterface = self.interfaceValues.currentRow()
        itemAddress = self.ipAddressValues.item( currentAddress )
        idAddress = self.address_to_id[itemAddress.text()]
        itemMac = self.macValues.item( currentMac )
        idMac = self.address_to_id[itemMac.text()]
        itemInterface = self.interfaceValues.item( currentInterface )
        idInterface =self.address_to_id[itemInterface.text()]
        self.addr.enableArp(str(idAddress))
        self.addr.enableArp( str( idMac ) )
        self.addr.enableArp( str( idInterface ) )
        itemAddress.setFlags( Qt.ItemIsSelectable )
        itemMac.setFlags( Qt.ItemIsSelectable)
        itemInterface.setFlags( Qt.ItemIsSelectable)

    def disableArp(self):
        currentAddress = self.ipAddressValues.currentRow()
        currentMac = self.macValues.currentRow()
        currentInterface = self.interfaceValues.currentRow()
        itemAddress = self.ipAddressValues.item( currentAddress )
        idAddress = self.address_to_id[itemAddress.text()]
        itemMac = self.macValues.item( currentMac )
        idMac = self.address_to_id[itemMac.text()]
        itemInterface = self.interfaceValues.item( currentInterface )
        idInterface = self.address_to_id[itemInterface.text()]
        print("Address is "+str(currentAddress))
        self.addr.disableArp( str(idAddress))
        self.addr.disableArp(str(currentMac))
        self.addr.disableArp(str(currentInterface))
        itemAddress.setFlags(Qt.NoItemFlags)
        itemMac.setFlags( Qt.NoItemFlags )
        itemInterface.setFlags( Qt.NoItemFlags )

    def removeArp(self):
        try:
            currentAddress = self.ipAddressValues.currentRow()
            currentMac = self.macValues.currentRow()
            currentInterface = self.interfaceValues.currentRow()
            itemAddress = self.ipAddressValues.item( currentAddress )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.removeArp(str(idAddress))
            self.listArp()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( "Cannot remove dynamic record" )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def init_buttons(self):
        print("text")
        self.addButton.clicked.connect( self.addArp )
        self.enableButton.clicked.connect( self.enableArp )
        self.disableButton.clicked.connect( self.disableArp )
        self.removeButton.clicked.connect( self.removeArp )
        self.refreshButton.clicked.connect( self.listArp )


