import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
#my designed file


qtCreatorFile = "./loginGUI/files.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class fileGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.listFiles()

    def listFiles(self):
        api = tikapy.TikapyClient(self.server)
        api.login(self.user,self.pwd)
        devices = api.talk(['/file/print'])
        self.fileField.clear()
        self.typeField.clear()
        self.sizeField.clear()
        self.timeField.clear()
        for i in devices:
            self.fileField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.sizeField.addItem(devices[i]['size'])
            self.timeField.addItem(devices[i]['creation-time'])

    def init_buttons(self):
        pass