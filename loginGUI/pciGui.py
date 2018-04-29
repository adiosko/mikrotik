import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.Resources import Resources
#my designed file


qtCreatorFile = "pci.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class pciGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = Resources(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listPci()

    def listPci(self):
        devices = self.addr.listPCIslots()
        self.deviceField.clear()
        self.vendorField.clear()
        self.nameField.clear()
        for i in devices:
            self.deviceField.addItem( devices[i]['device'] )
            self.vendorField.addItem(devices[i]['vendor'])
            self.nameField.addItem(devices[i]['name'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listPci )