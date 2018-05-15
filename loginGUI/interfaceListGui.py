import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.interfaceList import interfaceList
from loginGUI.addInterfaceList import addInterfaceListGui
#my designed file


qtCreatorFile = "./loginGUI/ifaceList.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class interfaceListGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = interfaceList(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listInterfaces()

    def listInterfaces(self):
        devices = self.addr.interfaceListMemenrPrint()
        self.nameField.clear()
        self.builtField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            statebuilt = ""
            try:
                state = devices[i]['name']
            except:
                state = "None"
            try:
                statebuilt = devices[i]['builtin']
            except:
                statebuilt = "Custom"
            self.builtField.addItem(statebuilt)
            self.nameField.addItem(state)
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def removeInterface(self):
        try:
            current = self.nameField.currentRow()
            itemName = self.nameField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeMemeber( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def addList(self):
        #self.nd = addInterfaceListGui(self.user,self.pwd,self.server,self)
        #self.nd.show()
        action = addInterfaceListGui( self.user, self.pwd, self.server, self )
        self.parent.mdi.addSubWindow( action )
        action.show()
        #self.mdi.cascadeSubWindows()


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.removeButton.clicked.connect(self.removeInterface)
        self.addButton.clicked.connect(self.addList)
