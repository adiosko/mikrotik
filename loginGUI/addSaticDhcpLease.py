from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from PyQt4.QtGui import *
from IPv4.DhcpServer import  DhcpServer
import sys
import tikapy

qtCreatorFile = "addStaticDhcpLease.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addStaticLease(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, route_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.route_window = route_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = DhcpServer( self.server, self.user, self.pwd )

    def okLogin(self):
        try:
            address = self.addressField.toPlainText()
            mac = self.macField.toPlainText()
            server = self.serverField.toPlainText()
            self.addr.addLease(address,mac,server)
            self.route_window.listAddresses()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Addiction error" )
            self.msg.setInformativeText( "Invalid arguments" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)