import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
from loginGUI.ipAddressesGui import ipAddressesGui
from loginGUI.arp import  arpGui
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
        self.menuQuit = self.menu.addMenu("About")
        #vytvorenie podtlacitka Addresses
        self.actionIP = QAction("Addresses", self)
        self.menuIP.addAction(self.actionIP)
        self.actionIP.triggered.connect(self.openAddressesWindow)
        #vytvorenie podtlacitka ARP
        self.actionArp =QAction("ARP",self)
        self.menuIP.addAction( self.actionArp )
        self.actionArp.triggered.connect( self.openArpWindow)
        #vytvorenie DHCP klient
        self.actionDhcpClient = QAction("DHCP Client",self)
        self.menuIP.addAction(self.actionDhcpClient)
        self.actionDhcpClient.triggered.connect(self.my_func1)
        # vytvorenie DHCP server
        self.actionDhcpServer = QAction( "DHCP Server", self )
        self.menuIP.addAction( self.actionDhcpServer )
        self.actionDhcpServer.triggered.connect( self.my_func1 )
        # vytvorenie Filter rules
        self.actionFilter = QAction( "Filter rules", self )
        self.menuIP.addAction( self.actionFilter )
        self.actionFilter.triggered.connect( self.my_func1 )
        # vytvorenie Filter rules
        self.actionNat = QAction( "NAT rules", self )
        self.menuIP.addAction( self.actionNat )
        self.actionNat.triggered.connect( self.my_func1 )
        # vytvorenie Firewall connection
        self.actionConnection = QAction( "Firewall connections", self )
        self.menuIP.addAction( self.actionConnection )
        self.actionConnection.triggered.connect( self.my_func1 )
        # vytvorenie Neighbors
        self.actionNeighbors = QAction( "Router neighbors", self )
        self.menuIP.addAction( self.actionNeighbors )
        self.actionNeighbors.triggered.connect( self.my_func1 )
        # vytvorenie Pool
        self.actionPool = QAction( "Pool", self )
        self.menuIP.addAction( self.actionPool )
        self.actionPool.triggered.connect( self.my_func1 )
        # vytvorenie Pool used addresses
        self.actionPoolAddr = QAction( "Pool used addresses", self )
        self.menuIP.addAction( self.actionPoolAddr )
        self.actionPoolAddr.triggered.connect( self.my_func1 )
        # vytvorenie Route list
        self.actionRouteList = QAction( "Route list", self )
        self.menuIP.addAction( self.actionRouteList )
        self.actionRouteList.triggered.connect( self.my_func1 )
        # vytvorenie Route nexthops
        self.actionRouteNExtHops = QAction( "RouteNext Hop", self )
        self.menuIP.addAction( self.actionRouteNExtHops )
        self.actionRouteNExtHops.triggered.connect( self.my_func1 )
        # vytvorenie Services
        self.actionServices = QAction( "Services IP", self )
        self.menuIP.addAction( self.actionServices )
        self.actionServices.triggered.connect( self.my_func1 )
        #System podmenu
        self.actionSystem = QAction("Info", self)
        self.menuSystem.addAction(self.actionSystem)
        self.actionSystem.triggered.connect(self.my_func1)
        #System Quit
        self.actionQuit = QAction("Quit",self)
        self.menuQuit.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)
        #System about
        self.actionAbout = QAction("About",self)
        self.menuQuit.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.about)


    def init_buttons(self):
        pass

    def openAddressesWindow(self):
        print("test")
        self.opened_window = ipAddressesGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def openArpWindow(self):
        print("arp")
        self.opened_window = arpGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def quit(self):
        sys.exit()

    def about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Diploma thesis software")
        msg.setInformativeText("Diploma thesis software")
        msg.setWindowTitle("About")


    def my_func1(self):
        print("test1")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginMikrotik()
    window.show()
    sys.exit(app.exec_())