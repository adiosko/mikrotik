import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from System.usersActive import UserActive
#my designed file


qtCreatorFile = "./loginGUI/userActive.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class usersActive(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = UserActive(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listUsers()

    def listUsers(self):
        devices = self.addr.listActiveUsers()
        self.userField.clear()
        self.atField.clear()
        self.fromField.clear()
        self.viaField.clear()
        self.groupField.clear()
        for i in devices:
            self.userField.addItem( devices[i]['name'] )
            self.atField.addItem(devices[i]['when'])
            self.fromField.addItem(devices[i]['address'])
            self.viaField.addItem( devices[i]['via'] )
            self.groupField.addItem( devices[i]['group'] )

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listUsers )