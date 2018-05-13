import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
#my designed file


qtCreatorFile = "./loginGUI/drivers.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class drivers(QtGui.QMainWindow,Ui_MainWindow):
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
        self.listDrivers()

    def listDrivers(self):
        api = tikapy.TikapyClient(self.server)
        api.login(self.user,self.pwd)
        devices = api.talk(['/driver/print'])
        self.driverField.clear()
        for i in devices:
            self.driverField.addItem( devices[i]['driver'] )

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listDrivers )