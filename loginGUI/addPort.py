from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from PyQt4.QtGui import QMessageBox

from bridge.BridgePorts import  BridgePorts
import sys

qtCreatorFile = "addPort.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addPortGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, arp_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.arp_window = arp_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = BridgePorts( self.server, self.user, self.pwd )

    def okLogin(self):
        try:
            interface = self.interfaceField.toPlainText()
            bridge = self.bridgeField.toPlainText()
            self.addr.addPort(interface,bridge)
            self.arp_window.listArp()
            self.close()
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Addiction error" )
            self.msg.setInformativeText( str(e) )
            self.msg.setWindowTitle( str( e.args[0] ) )
            self.msg.show()

    def cancelLogin(self):
         sys.exit()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)