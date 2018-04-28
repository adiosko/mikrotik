import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
from loginGUI.ipAddressesGui import ipAddressesGui
from loginGUI.arp import  arpGui
from loginGUI.Maintenance import Maintenance
#import  LoginManager
#my designed file
import tikapy
from loginGUI.packages import packages
from loginGUI.disk import disks
from loginGUI.drivers import drivers
from loginGUI.history import history
from loginGUI.logGui import logGui
from loginGUI.fileGui import fileGui
from loginGUI.restoreGui import restoreGui
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
        self.menuWireless = self.menu.addMenu( "Wireless" )
        self.menuBridge = self.menu.addMenu( "Bridge" )
        self.menuSystem = self.menu.addMenu( "System" )
        self.menuMaintenance = self.menu.addMenu("Maintenance")
        self.menuFiles = self.menu.addMenu( "Files" )
        self.menuLog = self.menu.addMenu("Log")
        self.menuQuit = self.menu.addMenu("About")
        #vytvorenie podtlacitka Addresses
        self.actionIP = QAction("Addresses", self)
        self.menuIP.addAction(self.actionIP)
        self.actionIP.triggered.connect(self.openAddressesWindow)
        # vytvorenie podtlacitka Files
        self.actionFiles = QAction( "File Manager", self )
        self.menuFiles.addAction( self.actionFiles )
        self.actionFiles.triggered.connect( self.files )
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
        #System Quit
        self.actionQuit = QAction("Quit",self)
        self.menuQuit.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.quit)
        #System about
        self.actionAbout = QAction("About",self)
        self.menuQuit.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.about)
        #Reboot
        self.actionReboot = QAction("Reboot",self)
        self.menuMaintenance.addAction(self.actionReboot)
        self.actionReboot.triggered.connect(self.reboot)
        #SHutdown
        self.actionShutdown = QAction("Shutdown",self)
        self.menuMaintenance.addAction(self.actionShutdown)
        self.actionShutdown.triggered.connect(self.shutdown)
        # Upgarde
        self.actionUpgrade = QAction( "Upgarde ROS", self )
        self.menuMaintenance.addAction( self.actionUpgrade )
        self.actionUpgrade.triggered.connect( self.upgrade )
        # Packages
        self.actionPackages = QAction( "Package manager", self )
        self.menuMaintenance.addAction( self.actionPackages )
        self.actionPackages.triggered.connect( self.package )
        #Disks
        self.actionDisks = QAction("System disks", self)
        self.menuSystem.addAction(self.actionDisks)
        self.actionDisks.triggered.connect(self.disks)
        #Driver
        self.actionDriver = QAction( "System driver", self )
        self.menuSystem.addAction( self.actionDriver )
        self.actionDriver.triggered.connect( self.driver )
        #History
        self.actionHistory = QAction( "System history", self )
        self.menuSystem.addAction( self.actionHistory )
        self.actionHistory.triggered.connect( self.history )
        #Hostname
        self.actionIdentity = QAction( "System hostname", self )
        self.menuSystem.addAction( self.actionIdentity )
        self.actionIdentity.triggered.connect( self.identity )
        #Reset Config
        self.actionReset = QAction( "Reset configuration", self )
        self.menuSystem.addAction( self.actionReset )
        self.actionReset.triggered.connect( self.reset )
        #Resource IRQ
        self.actionIrq = QAction( "IRQ info", self )
        self.menuSystem.addAction( self.actionIrq )
        self.actionIrq.triggered.connect( self.irq )
        #Resource CPU
        self.actionCpu = QAction( "CPU info", self )
        self.menuSystem.addAction( self.actionCpu )
        self.actionCpu.triggered.connect( self.cpu )
        #Users
        self.actionUsers = QAction( "System users", self )
        self.menuSystem.addAction( self.actionUsers )
        self.actionUsers.triggered.connect( self.users )
        #Usergroup
        self.actionGroup = QAction( "System user groups", self )
        self.menuSystem.addAction( self.actionGroup )
        self.actionGroup.triggered.connect( self.group)
        #log
        self.actionLog = QAction( "Log", self )
        self.menuLog.addAction( self.actionLog )
        self.actionLog.triggered.connect( self.log )
        #restore
        self.actionRestore = QAction("Restore configuration",self)
        self.menuMaintenance .addAction(self.actionRestore)
        self.actionRestore.triggered.connect(self.restore)

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

    def reboot(self):
        api = tikapy.TikapyClient(self.server)
        api.login(self.user,self.pwd)
        api.talk(['/system/reboot'])
        sys.exit()

    def shutdown(self):
        api = tikapy.TikapyClient( self.server )
        api.login( self.user, self.pwd )
        api.talk( ['/system/shutdown'] )
        sys.exit()

    def upgrade(self):
        api = tikapy.TikapyClient( self.server )
        api.login( self.user, self.pwd )
        api.talk( ['/system/upgrade/download-all'] )

    def package(self):
        self.opened_window = packages( self.user, self.pwd, self.server )
        self.opened_window.show()

    def disks(self):
        self.opened_window = disks(self.user,self.pwd,self.server)
        self.opened_window.show()

    def driver(self):
        self.opened_window = drivers(self.user,self.pwd,self.server)
        self.opened_window.show()

    def files(self):
        self.opened_window = fileGui( self.user, self.pwd, self.server )
        self.opened_window.show()

    def history(self):
        self.opened_window = history(self.user,self.pwd,self.server)
        self.opened_window.show()

    def log(self):
        self.opened_window = logGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def restore(self):
        self.opened_window = restoreGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def identity(self):
        pass

    def reset(self):
        pass

    def irq(self):
        pass

    def cpu(self):
        pass

    def users(self):
        pass

    def group(self):
        pass


    def my_func1(self):
        print("test1")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginMikrotik()
    window.show()
    sys.exit(app.exec_())