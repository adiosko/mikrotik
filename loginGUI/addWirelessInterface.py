from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from PyQt4 import *
from PyQt4.QtGui import QMessageBox

from wireless.interfaces import  interfaces
import sys

qtCreatorFile = "./loginGUI/addWirelessInterface.ui"

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
        try:
            name = self.nameField.toPlainText()
            master = self.masterField.toPlainText()
            secirity = self.securityField.toPlainText()
            vlan = self.vlanField.toPlainText()
            self.addr.addInterface(name,master,secirity,vlan)
            self.wireless_window.listInterfaces()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Master interface error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
         self.close()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)