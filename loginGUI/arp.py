import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
from loginGUI.addAddressGui import addAddressGui
#my designed file
from IPv4.Arp import  Arp
from loginGUI.addArpGui import addArpGui

qtCreatorFile = "./loginGUI/arp.ui"

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
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            self.ipAddressValues.addItem( devices[i]['address'])
            try:
                state = devices[i]['mac-address']
            except:
                state = "None"
            self.macValues.addItem( state)
            self.interfaceValues.addItem(devices[i]['interface'])
            self.dynamicField.addItem(devices[i]['dynamic'])
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['address']] = devices[i]['.id']

    def addArp(self):
        #self.nd = addArpGui(self.user, self.pwd, self.server,self)
        #self.nd.show()
        action = addArpGui( self.user, self.pwd, self.server, self)
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()

    def enableArp(self):
        try:
            currentAddress = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( currentAddress )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.enableArp(str(idAddress))
            self.listArp()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Enable item error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()


    def disableArp(self):
        try:
            currentAddress = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( currentAddress )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.disableArp( str( idAddress ) )
            self.listArp()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Disable item error" )
            self.msg.setInformativeText( "Cannot disable dynamic record" )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def removeArp(self):
        try:
            currentAddress = self.ipAddressValues.currentRow()
            itemAddress = self.ipAddressValues.item( currentAddress )
            idAddress = self.address_to_id[itemAddress.text()]
            self.addr.removeArp( str( idAddress ) )
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


