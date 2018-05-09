import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from IPv4.DhcpServer import  DhcpServer
from loginGUI.addPoolGui import addPool

qtCreatorFile = "addDhcpServer.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addDhcpServerGui(QtGui.QMainWindow,Ui_MainWindow):
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
        self.addr = DhcpServer(self.server,self.user,self.pwd)

    def okLogin(self):
        try:
            name = self.nameField.toPlainText()
            interface = self.interfaceField.toPlainText()
            pool = self.poolField.toPlainText()
            server = self.serverField.toPlainText()
            lease = self.leaseField.toPlainText()
            self.addr.addDhcp(name,interface,pool,server,lease)
            self.address_window.listAddresses()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    """    
    def pool(self):
        self.nd = addPool( self.user, self.pwd, self.server)
        self.nd.show()
    """


    def cancelLogin(self):
        self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)
        #self.poolButton.clicked.connect(self.okLogin)