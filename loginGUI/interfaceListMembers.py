import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.interfaceList import interfaceList
from loginGUI.addListMemeberGui import addListMemberGui
#my designed file


qtCreatorFile = "./loginGUI/interfaceListMemebers.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class interfaceListMemberGui(QtGui.QMainWindow,Ui_MainWindow):
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
        devices = self.addr.listInterafce()
        self.listField.clear()
        self.interfaceField.clear()
        self.disableField.clear()
        self.address_to_id = {}
        for i in devices:
            state = ""
            statedisable = ""
            self.listField.addItem(devices[i]['list'])
            self.interfaceField.addItem(devices[i]['interface'])
            self.disableField.addItem( devices[i]['disabled'] )
            self.address_to_id[devices[i]['list']] = devices[i]['.id']

    def removeInterface(self):
        try:
            current = self.listField.currentRow()
            itemName = self.listField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.removeList( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def enableInterface(self):
        try:
            current = self.listField.currentRow()
            itemName = self.listField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.enableList( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def disableInterface(self):
        try:
            current = self.listField.currentRow()
            itemName = self.listField.item( current )
            idName = self.address_to_id[itemName.text()]
            self.addr.disableList( str( idName) )
            self.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Remove error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def addList(self):
        self.nd = addListMemberGui(self.user,self.pwd,self.server,self)
        self.nd.show()


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )
        self.removeButton.clicked.connect(self.removeInterface)
        self.addButton.clicked.connect(self.addList)
        self.disableButton.clicked.connect(self.disableInterface)
        self.enableButton.clicked.connect(self.enableInterface)
