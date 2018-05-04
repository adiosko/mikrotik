import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.NeighborLIst import NeighborList
#my designed file


qtCreatorFile = "neighbor.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class neighborList(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = NeighborList(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listNeighbors()

    def listNeighbors(self):
        devices = self.addr.listNeighbors()
        self.interfaceField.clear()
        self.ipField.clear()
        self.macField.clear()
        self.platformField.clear()
        self.versionField.clear()
        self.identityField.clear()
        for i in devices:
            self.interfaceField.addItem( devices[i]['interface'] )
            state = ""
            try:
                devices[i]['address']
            except:
                state = "none"
            self.macField.addItem(devices[i]['mac-address'])
            try:
                devices[i]['platform']
            except:
                state = "Unknown"
            try:
                devices[i]['version']
            except:
                state = "Unknown"
            try:
                devices[i]['identity']
            except:
                state = "Unknown"


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listNeighbors )