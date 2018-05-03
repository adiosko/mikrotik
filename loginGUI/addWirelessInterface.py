from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from wireless.interfaces import  interfaces
import sys

qtCreatorFile = "addWirelessInterface.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addWirelessInterfaceGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, wireless_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.wireless_window = wireless_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = interfaces( self.server, self.user, self.pwd )

    def okLogin(self):
        name = self.nameField.toPlainText()
        master = self.masterField.toPlainText()
        secirity = self.securityField.toPlainText()
        vlan = self.vlanField.toPlainText()
        self.addr.addInterface(name,master,secirity,vlan)
        self.wireless_window.listInterfaces()
        self.close()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)