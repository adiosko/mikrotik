import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.History import History
#my designed file


qtCreatorFile = "./loginGUI/history.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class history(QtGui.QWidget,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        #super().__init__( self, None, QtCore.Qt.WindowStaysOnTopHint )
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = History(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listHistory()

    def listHistory(self):
        devices = self.addr.listHistory()
        self.timeField.clear()
        for i in devices:
            self.timeField.addItem( devices[i]['time'] + "\t"+devices[i]['action']+"\t"+devices[i]['by']+"\t"+devices[i]['policy'])

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listHistory )