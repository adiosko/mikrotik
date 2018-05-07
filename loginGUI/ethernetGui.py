import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.ethernet import ethernet
#my designed file


qtCreatorFile = "ethernet.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ethernetGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = ethernet(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listInterfaces()

    def listInterfaces(self):
        devices = self.addr.printInterface()
        self.nameField.clear()
        self.mtuField.clear()
        self.speedField.clear()
        self.macField.clear()
        self.txField.clear()
        self.rxField.clear()
        self.disableField.clear()
        self.runField.clear()
        self.address_to_id = {}
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.mtuField.addItem(devices[i]['mtu'])
            self.speedField.addItem(devices[i]['speed'])
            self.macField.addItem( devices[i]['mac-address'] )
            self.txField.addItem(devices[i]['tx-bytes'])
            self.rxField.addItem(devices[i]['rx-bytes'])
            self.disableField.addItem(devices[i]['disabled'])
            self.runField.addItem(devices[i]['running'])
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
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def resetInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.resetMac( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Port error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.enableButton.clicked.connect(self.enableInterface)
        self.disableButton.clicked.connect(self.disableInterface)
        self.powerButton.clicked.connect(self.resetInterface)
