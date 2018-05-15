import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#from loginGUI.loginWindow import loginMikrotik
#my designed file
from IPv4.Addresses import  Addresses
#from loginGUI.loginWindow import loginMikrotik

qtCreatorFile = "./loginGUI/ipAddresses.ui"

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
        #self.parent = loginMikrotik(self.user,self.pwd,self.server, self)
        #self.mdi = QMdiArea()
        #self.setCentralWidget( self.mdi )
        self.init_buttons()
        #self.address_to_id = {}
        self.addr = Addresses(self.server,self.user,self.pwd)
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listAddresses()
        self.ipAddressValues.clear()
        self.networkValues.clear()
        self.interfaceValues.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            self.ipAddressValues.addItem( devices[i]['address'])
            self.networkValues.addItem(devices[i]['network'])
            self.interfaceValues.addItem(devices[i]['interface'])
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['address']] = devices[i]['.id']

    def addAddress(self):
        #self.nd = addAddressGui(self.user,self.pwd,self.server, self)
        #self.nd.show()
        action = addAddressGui( self.user, self.pwd, self.server, self)
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()


    def enableAddress(self):
        try:
            current = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( current )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.enableAddress(str(idAddress))
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disableAddress(self):
        try:
            current = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( current )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.disableAddress( str( idAddress ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Disable error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def removeAddress(self):
        try:
            current = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( current )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.removeAddress( str( idAddress ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def init_buttons(self):
        self.addButton.clicked.connect( self.addAddress )
        self.enableButton.clicked.connect(self.enableAddress)
        self.disableButton.clicked.connect(self.disableAddress)
        self.removeButton.clicked.connect(self.removeAddress)
        self.refreshButton.clicked.connect( self.listAddresses )
        #self.editButton.clicked.connect(self.setInterface)
