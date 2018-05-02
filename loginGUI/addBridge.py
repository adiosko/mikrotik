from PyQt4 import QtCore, QtGui, uic
#import  LoginManager
#my designed file
from bridge.BridgeGeneral import  BridgeGeneral
import sys

qtCreatorFile = "addBridge.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class addBridgeGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd, server, bridge_window):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.bridge_window = bridge_window
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        self.addr = BridgeGeneral( self.server, self.user, self.pwd )

    def okLogin(self):
        name = self.nameField.toPlainText()
        protocol = self.protocolField.toPlainText()
        self.addr.addBridge(name,protocol)
        self.bridge_window.listBridge()

    def cancelLogin(self):
         sys.exit()

    def init_buttons(self):
        self.cancelButton.clicked.connect(self.cancelLogin)
        self.okButton.clicked.connect(self.okLogin)