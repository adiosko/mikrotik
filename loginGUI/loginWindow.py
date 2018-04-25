import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
from loginGUI.ipAddressesGui import ipAddressesGui
#import  LoginManager
#my designed file
qtCreatorFile = "loginWIndow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class loginMikrotik(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user,pwd,server):
        #super( loginMikrotik, self ).__init__( )
        #self.setupUi(self)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.user = user
        self.pwd = pwd
        self.server = server
        self.setupUi(self)
        self.init_buttons()
        #sablona mikrotik tlacitka a menu (vytvorenie IP tlacitka)
        self.menu = self.menuBar()
        #velke menu
        self.menuIP = self.menu.addMenu("IP")
        self.menuSystem = self.menu.addMenu( "System" )
        #vytvorenie podtlacitka
        self.actionIP = QAction("Addresses", self)
        self.menuIP.addAction(self.actionIP)
        self.actionIP.triggered.connect(self.openAddressesWindow)
        #System podmenu
        self.actionSystem = QAction("Info", self)
        self.menuSystem.addAction(self.actionSystem)
        self.actionSystem.triggered.connect(self.my_func1)

    def init_buttons(self):
        pass

    def openAddressesWindow(self):
        print("test")
        self.opened_window = ipAddressesGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def my_func1(self):
        print("test1")
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginMikrotik()
    window.show()
    sys.exit(app.exec_())