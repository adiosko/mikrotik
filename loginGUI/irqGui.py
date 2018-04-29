import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.Resources import Resources
#my designed file


qtCreatorFile = "irq.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class irqGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.listIrq()

    def listIrq(self):
        devices = self.addr.listIRQ()
        self.irqField.clear()
        self.userField.clear()
        self.connectionField.clear()
        self.countField.clear()
        for i in devices:
            self.irqField.addItem( devices[i]['irq'] )
            self.userField.addItem(devices[i]['users'])
            self.connectionField.addItem(devices[i]['cpu'])
            self.countField.addItem(devices[i]['per-cpu-count'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listIrq )