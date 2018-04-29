import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.Resources import Resources
#my designed file


qtCreatorFile = "cpu.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class cpuGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.listCpu()

    def listCpu(self):
        devices = self.addr.listCPUInfo()
        self.cpuField.clear()
        self.loadField.clear()
        self.irqField.clear()
        self.diskField.clear()
        for i in devices:
            self.cpuField.addItem( devices[i]['cpu'] )
            self.loadField.addItem(devices[i]['load'])
            self.irqField.addItem(devices[i]['irq'])
            self.diskField.addItem(devices[i]['disk'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listCpu )