import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from IPv4.FirewallNAT import  FirewallNAT

qtCreatorFile = "addMasquarade.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addMasquaradeGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, address_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.address_window = address_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = FirewallNAT(self.server,self.user,self.pwd)

    def okLogin(self):
        try:
            interface = self.interfaceField.toPlainText()
            self.addr.addMasquarade(interface)
            self.address_window.listNat()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Interface error" )
            self.msg.setInformativeText( "Wrong interface" )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
        self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)