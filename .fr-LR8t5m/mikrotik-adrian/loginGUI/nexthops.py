import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.RouteNexthops import RouteNexthops
#from loginGUI.addProfile import addProfile
#my designed file


qtCreatorFile = "./loginGUI/nexthop.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class nextHopGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = RouteNexthops(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listServices()

    def listServices(self):
        devices = self.addr.listNexthops()
        self.addressField.clear()
        self.gwField.clear()
        self.scopeField.clear()
        self.address_to_id = {}
        for i in devices:
            self.addressField.addItem( devices[i]['address'] )
            self.gwField.addItem(devices[i]['gw-state'])
            self.scopeField.addItem(devices[i]['scope'])
            self.address_to_id[devices[i]['address']] = devices[i]['.id']

    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listServices )