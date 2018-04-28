import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
#my designed file


qtCreatorFile = "restore.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class restoreGui(QtGui.QMainWindow,Ui_MainWindow):
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

    def restoreConfiguration(self):
        file = self.fileField.toPlainText()
        password = self.passwordField.toPlainText()
        api = tikapy.TikapyClient(self.server)
        api.login(self.user,self.pwd)
        api.talk(['/system/backup/load','=name='+file,'=password='+password])


    def init_buttons(self):
        self.restoreButton.clicked.connect( self.restoreConfiguration )
