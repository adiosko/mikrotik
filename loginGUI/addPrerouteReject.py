import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from IPv4.FirewallMangle import  FirewallMangle

qtCreatorFile = "./loginGUI/addMaglePost.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addManglePrerouteReject(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = FirewallMangle(self.server,self.user,self.pwd)

    def okLogin(self):
        try:
            protocol = self.protField.toPlainText()
            srcport = self.sportField.toPlainText()
            dstport = self.dportField.toPlainText()
            srcaddr = self.srcField.toPlainText()
            dstaddr = self.dstField.toPlainText()
            self.addr.addPreroutingreject(dstaddr,srcaddr,protocol,srcport,dstport)
            self.address_window.listRules()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Input error " )
            self.msg.setInformativeText(str(e))
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
        self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)