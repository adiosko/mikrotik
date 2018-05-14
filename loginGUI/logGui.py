import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from loginGUI.Log import Log
#my designed file


qtCreatorFile = "./loginGUI/log.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class logGui(QtGui.QWidget,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = Log(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listlog()

    def listlog(self):
        devices = self.addr.listLog()
        self.timeField.clear()
        for i in devices:
            self.timeField.addItem( devices[i]['time'] +"\t"+ devices[i]['topics']+"\t"+devices[i]['message'])


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listlog )