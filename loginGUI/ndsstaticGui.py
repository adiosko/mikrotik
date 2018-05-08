import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DNSstatic import DNSstatic
from loginGUI.addStaticDnsGui import addStaticGui
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "dnstatic.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dnsstaticGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DNSstatic(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listRecords()
        self.nameField.clear()
        self.addressField.clear()
        self.ttlField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            statettl = ""
            self.nameField.addItem( devices[i]['name'] )
            self.addressField.addItem(devices[i]['address'])
            try:
                statettl = devices[i]['ttl']
            except:
                statettl = "None"
            self.ttlField.addItem( statettl)
            self.disableField.addItem(devices[i]['disabled'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def enableItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableRecord( str( idName ) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Enable item error" )
            self.msg.setInformativeText( str(e))
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def disableItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableRecord( str( idName) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Disable error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def removeItem(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeRecord( str( idName) )
            self.listAddresses()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Item erro" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def addItem(self):
        self.nd = addStaticGui(self.user, self.pwd, self.server,self)
        self.nd.show()


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses )
        self.addButton.clicked.connect(self.addItem)
        self.removeButton.clicked.connect(self.removeItem)
        self.enableButton.clicked.connect(self.enableItem)
        self.disableButton.clicked.connect(self.disableItem)