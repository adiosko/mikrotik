import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DNScache import DNScache
#from loginGUI.addStaticDnsGui import addStaticGui
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "./loginGUI/dnscache.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dnscacheGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DNScache(self.server,self.user,self.pwd)
        self.init_buttons()
        self.listCache()

    def listCache(self):
        devices = self.addr.listCache()
        self.nameField.clear()
        self.typeField.clear()
        self.dataField.clear()
        self.ttlField.clear()
        self.address_to_id = {}
        for i in devices:
            statettl = ""
            self.nameField.addItem( devices[i]['name'] )
            self.typeField.addItem(devices[i]['type'])
            self.dataField.addItem(devices[i]['data'])
            self.ttlField.addItem(devices[i]['ttl'])
            self.address_to_id[devices[i]['name']] = devices[i]['.id']

    def flushDNS(self):
        try:
            self.addr.flushDNS()
            self.listCache()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "DNS error" )
            self.msg.setInformativeText(str(e) )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()


    def init_buttons(self):
        self.refreshButton.clicked.connect( self.listCache)
        self.flushButton.clicked.connect(self.flushDNS)