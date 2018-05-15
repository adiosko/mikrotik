import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.vlan import vlan
from loginGUI.addInterfaceVlanGui import addVLANInterfaceGui
#my designed file


qtCreatorFile = "./loginGUI/interfaceVlan.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class interfaceVlanGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = vlan(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listInterfaces()

    def listInterfaces(self):
        devices = self.addr.listVlan()
        self.nameField.clear()
        self.mtuField.clear()
        self.interfaceField.clear()
        self.macField.clear()
        self.disabledField.clear()
        self.runField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            self.nameField.addItem(devices[i]['name'])
            self.mtuField.addItem(devices[i]['mtu'])
            self.interfaceField.addItem(devices[i]['interface'])
            self.macField.addItem(devices[i]['mac-address'])
            self.disabledField.addItem(devices[i]['disabled'])
            self.runField.addItem(devices[i]['running'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def removeInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeVlan( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "VLAN errror")
            self.msg.setInformativeText( str(e))
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def enableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableVlan( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Enable error" )
            self.msg.setInformativeText(str(e))
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disableInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableVlan( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Disable error" )
            self.msg.setInformativeText(str(e))
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def addList(self):
        #self.nd = addVLANInterfaceGui(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addVLANInterfaceGui( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces)
        self.removeButton.clicked.connect(self.removeInterface)
        self.addButton.clicked.connect(self.addList)
        self.enableButton.clicked.connect(self.enableInterface)
        self.disableButton.clicked.connect(self.disableInterface)
