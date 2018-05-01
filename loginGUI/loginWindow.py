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
from loginGUI.resetGui import resetGui
from loginGUI.hostname import hostnameGui
from loginGUI.irqGui import irqGui
from loginGUI.cpuGui import cpuGui
from loginGUI.usbGui import usbGui
from loginGUI.pciGui import pciGui
from loginGUI.usersActiveGui import usersActive
from loginGUI.usersGui import usersGui
from loginGUI.interfacesGui import interfaceGui
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
        self.menuInterface = self.menu.addMenu("Interface")
        self.menuIP = self.menu.addMenu("IP")
        self.menuWireless = self.menu.addMenu( "Wireless" )
        self.menuBridge = self.menu.addMenu( "Bridge" )
        self.menuSystem = self.menu.addMenu( "System" )
        self.menuMaintenance = self.menu.addMenu("Maintenance")
        #iface menu
        self.actionInterface = QAction("Interfaces",self)
        self.menuInterface.addAction(self.actionInterface)
        self.actionInterface.triggered.connect(self.interfaces)
        # iface menu
        self.actionEthernet= QAction( "Ethernet", self )
        self.menuInterface.addAction( self.actionEthernet )
        self.actionEthernet.triggered.connect( self.ethernet )
        #vlan
        self.actionVLAN = QAction( "VLAN", self )
        self.menuInterface.addAction( self.actionVLAN )
        self.actionVLAN.triggered.connect( self.vlan )
        #Connections
        self.actionIfaceCon = QAction( "Connections", self )
        self.menuInterface.addAction( self.actionIfaceCon )
        self.actionIfaceCon.triggered.connect( self.interfaceConnections )
        #self.menuFiles = self.menu.addMenu( "Files" )
        self.menuLog = self.menu.addMenu("Log")
        self.menuQuit = self.menu.addMenu("About")
        #vytvorenie podtlacitka Addresses
        self.actionIP = QAction("Addresses", self)
        self.menuIP.addAction(self.actionIP)
        self.actionIP.triggered.connect(self.openAddressesWindow)
        # vytvorenie podtlacitka Files
        #self.actionFiles = QAction( "File Manager", self )
        #self.menuFiles.addAction( self.actionFiles )
        #self.actionFiles.triggered.connect( self.files )
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
        # vytvorenie DHCP server leases
        self.actionDhcpServerLeases = QAction( "DHCP Assigned Addresses", self )
        self.menuIP.addAction( self.actionDhcpServerLeases )
        self.actionDhcpServerLeases.triggered.connect( self.my_func1 )
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
        self.actionIdentity.triggered.connect( self.identity)
        #Reset Config
        self.actionReset = QAction( "Reset configuration", self )
        self.menuMaintenance.addAction( self.actionReset )
        self.actionReset.triggered.connect( self.reset )
        #Resource IRQ
        self.actionIrq = QAction( "IRQ info", self )
        self.menuSystem.addAction( self.actionIrq )
        self.actionIrq.triggered.connect( self.irq )
        #Resource CPU
        self.actionCpu = QAction( "CPU info", self )
        self.menuSystem.addAction( self.actionCpu )
        self.actionCpu.triggered.connect( self.cpu )
        # Resource USB
        self.actionUsb = QAction( "USB info", self )
        self.menuSystem.addAction( self.actionUsb )
        self.actionUsb.triggered.connect( self.usb)
        # Resource PCI
        self.actionPci = QAction( "PCI info", self )
        self.menuSystem.addAction( self.actionPci)
        self.actionPci.triggered.connect( self.pci )
        #Users
        self.actionUsers = QAction( "System users", self )
        self.menuSystem.addAction( self.actionUsers )
        self.actionUsers.triggered.connect( self.users )
        #Active users
        self.actionGroup = QAction( "Active users", self )
        self.menuSystem.addAction( self.actionGroup )
        self.actionGroup.triggered.connect( self.listUsers)
        #log
        self.actionLog = QAction( "Log", self )
        self.menuLog.addAction( self.actionLog )
        self.actionLog.triggered.connect( self.log )
        #restore
        self.actionRestore = QAction("Restore configuration",self)
        self.menuMaintenance.addAction(self.actionRestore)
        self.actionRestore.triggered.connect(self.restore)
        #Bridge global
        self.actionBridge = QAction("Bridge",self)
        self.menuBridge.addAction(self.actionBridge)
        self.actionBridge.triggered.connect(self.my_func1)
        #Bridge ports
        self.actionBridgePort = QAction( "Ports", self )
        self.menuBridge.addAction( self.actionBridgePort )
        self.actionBridgePort.triggered.connect( self.my_func1 )
        # Bridge VLAN
        self.actionBridgeVlan = QAction( "VLAN", self )
        self.menuBridge.addAction( self.actionBridgeVlan )
        self.actionBridgeVlan.triggered.connect( self.my_func1 )
        # Bridge connections
        self.actionBridgeConnections = QAction( "Connections", self )
        self.menuBridge.addAction( self.actionBridgeConnections )
        self.actionBridgeConnections.triggered.connect( self.my_func1 )
        # Wireless
        self.actionWifi = QAction( "Virtual interface", self )
        self.menuWireless.addAction( self.actionWifi )
        self.actionWifi.triggered.connect( self.my_func1 )
        # Wireless Security
        self.actionWifiSec = QAction( "Security", self )
        self.menuWireless.addAction( self.actionWifiSec )
        self.actionWifiSec.triggered.connect( self.my_func1 )
        # Wireless conenctions
        self.actionWifiCon = QAction( "Connection list", self )
        self.menuWireless.addAction( self.actionWifiCon )
        self.actionWifiCon.triggered.connect( self.my_func1 )

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
        self.opened_window = hostnameGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def reset(self):
        self.opened_window = resetGui( self.user, self.pwd, self.server )
        self.opened_window.show()

    def irq(self):
        self.opened_window = irqGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def cpu(self):
        self.opened_window = cpuGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def usb(self):
        self.opened_window = usbGui( self.user, self.pwd, self.server )
        self.opened_window.show()

    def pci(self):
        self.opened_window = pciGui( self.user, self.pwd, self.server )
        self.opened_window.show()

    def listUsers(self):
        self.opened_window = usersActive(self.user,self.pwd,self.server)
        self.opened_window.show()

    def users(self):
        self.opened_window = usersGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def interfaces(self):
        self.opened_window = interfaceGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def ethernet(self):
        pass

    def vlan(self):
        pass

    def interfaceConnections(self):
        pass


    def my_func1(self):
        print("test1")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= loginMikrotik()
    window.show()
    sys.exit(app.exec_())