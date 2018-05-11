import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.PoolUsedAddresses import PoolUsedAddresses
#from loginGUI.addProfile import addProfile
#my designed file


qtCreatorFile = "./loginGUI/poolUsed.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class poolUsedGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = PoolUsedAddresses(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listAddresses()

    def listAddresses(self):
        devices = self.addr.listAddresses()
        self.poolField.clear()
        self.addressField.clear()
        self.ownerField.clear()
        self.infoField.clear()
        self.address_to_id = {}
        for i in devices:
            self.poolField.addItem( devices[i]['pool'] )
            self.addressField.addItem(devices[i]['address'])
            self.ownerField.addItem(devices[i]['owner'])
            self.infoField.addItem(devices[i]['info'])
            self.address_to_id[devices[i]['pool']] = devices[i]['.id']

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listAddresses )