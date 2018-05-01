import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from interfaces.interfaces import interfaces
#my designed file


qtCreatorFile = "interfaces.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class interfaceGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = interfaces(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listInterfaces()

    def listInterfaces(self):
        devices = self.addr.listInterfaces()
        self.nameField.clear()
        self.typeField.clear()
        self.linkdownField.clear()
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.linkdownField.addItem(devices[i]['link-downs'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listInterfaces )