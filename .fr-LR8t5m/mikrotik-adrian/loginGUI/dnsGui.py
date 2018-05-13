import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
import tikapy
from IPv4.DNSglobal import DNSglobal
from loginGUI.addAddressListGui import addAddressListGui
#my designed file


qtCreatorFile = "./loginGUI/dns.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dnsGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.addr = DNSglobal(self.server,self.user,self.pwd)
        self.init_buttons()

    def okLogin(self):
        try:
            name = self.serverField.toPlainText()
            self.addr.setServers(name)
            self.close()
        except Exception as e:
            from PyQt4.QtGui import QMessageBox
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Cannot add server" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)