import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
#my designed file
from System.PackageManager import PackageManager

qtCreatorFile = "./loginGUI/disk.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class disks(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = PackageManager(self.server,self.user,self.pwd)
        self.listDisks()

    def listDisks(self):
        api = tikapy.TikapyClient(self.server)
        api.login(self.user,self.pwd)
        devices = api.talk(['/disk/print'])
        self.nameField.clear()
        self.labelField.clear()
        self.freeField.clear()
        self.sizeField.clear()
        for i in devices:
            self.nameField.addItem( devices[i]['name'] )
            self.labelField.addItem( devices[i]['label'] )
            self.freeField.addItem( devices[i]['free'] )
            self.sizeField.addItem(devices[i]['size'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listDisks )
