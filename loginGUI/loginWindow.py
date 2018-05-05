import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, uic
from loginGUI.ipAddressesGui import ipAddressesGui
from loginGUI.arp import  arpGui
from loginGUI.bridgePorts import bridgePort
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
from loginGUI.bridgeConnections import bridgeConnections
from loginGUI.bridgeVlan import bridgeVLAN
from loginGUI.bridgeGui import bridgeGUI
from loginGUI.WirelessInterfacesGui import wirelessInterfaceGui
from loginGUI.securityGui import securityGui
from loginGUI.registrationTable import registrationGui
from loginGUI.servicesGui import servicesGui
from loginGUI.nexthops import nextHopGui
from loginGUI.poolUsedAddresses import poolUsedGui
from loginGUI.routeGui import routeGui
from loginGUI.poolGui import poolGui
from loginGUI.neighborGui import neighborList
from loginGUI.firewallConnectionList import fwConnection
from loginGUI.filterGui import  fwGui
from loginGUI.natGui import natGui
from loginGUI.serviceportGui import  servicePortGui
from loginGUI.addresslistGui import addresslistGui
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
        self.setWindowTitle( user + "@" + server )
        self.init_buttons()
        #sablona mikrotik tlacitka a menu (vytvorenie IP tlacitka)
        self.menu = self.menuBar()
        #velke menu
        self.menuInterface = self.menu.addMenu("Interface")
        self.menuIP = self.menu.addMenu("IP")
        self.menuDhcp = self.menu.addMenu("DHCP")
        self.menuDns = self.menu.addMenu( "DNS" )
        self.menuPool = self.menu.addMenu("Address pools")
        self.menuRoute = self.menu.addMenu("Routing management")
        self.menuFirewall = self.menu.addMenu( "Firewall" )
        self.menuWireless = self.menu.addMenu( "Wireless" )
        self.menuBridge = self.menu.addMenu( "Bridge" )
        self.menuSystem = self.menu.addMenu( "Hostname" )
        self.menuSystemInfo = self.menu.addMenu("System information")
        self.menuUser = self.menu.addMenu("User management")
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
        self.menuDhcp.addAction(self.actionDhcpClient)
        self.actionDhcpClient.triggered.connect(self.my_func1)
        #dhcp relay
        self.actionRelay = QAction("DHCP Relay",self)
        self.menuDhcp.addAction(self.actionRelay)
        self.actionRelay.triggered.connect(self.my_func1)
        # vytvorenie DHCP server
        self.actionDhcpServer = QAction( "DHCP Server", self )
        self.menuDhcp.addAction( self.actionDhcpServer )
        self.actionDhcpServer.triggered.connect( self.my_func1 )
        # vytvorenie DHCP server leases
        self.actionDhcpServerLeases = QAction( "DHCP Assigned Addresses", self )
        self.menuDhcp.addAction( self.actionDhcpServerLeases )
        self.actionDhcpServerLeases.triggered.connect( self.my_func1 )
        #DNS
        self.actionDNS = QAction("Add server",self)
        self.menuDns.addAction(self.actionDNS)
        self.actionDNS.triggered.connect(self.my_func1)
        #DNS static record
        self.actionDNS = QAction( "Static records", self )
        self.menuDns.addAction( self.actionDNS )
        self.actionDNS.triggered.connect( self.staticrecord )
        # vytvorenie Filter rules
        self.actionFilter = QAction( "Filter rules", self )
        self.menuFirewall.addAction( self.actionFilter )
        self.actionFilter.triggered.connect( self.filter )
        # vytvorenie Filter rules
        self.actionNat = QAction( "NAT rules", self )
        self.menuFirewall.addAction( self.actionNat )
        self.actionNat.triggered.connect( self.nat )
        # vytvorenie Firewall connection
        self.actionConnection = QAction( "Connections", self )
        self.menuFirewall.addAction( self.actionConnection )
        self.actionConnection.triggered.connect( self.fwcon )
        #Firewall service port
        self.actionsport = QAction("Service ports",self)
        self.menuFirewall.addAction(self.actionsport)
        self.actionsport.triggered.connect(self.serviceport)
        #Address list
        self.actionadresslist = QAction( "Address list", self )
        self.menuFirewall.addAction( self.actionadresslist )
        self.actionadresslist.triggered.connect( self.addressList )
        # vytvorenie Neighbors
        self.actionNeighbors = QAction( "Router neighbors", self )
        self.menuRoute.addAction( self.actionNeighbors )
        self.actionNeighbors.triggered.connect( self.neighbors )
        # vytvorenie Pool
        self.actionPool = QAction( "Pool", self )
        self.menuPool.addAction( self.actionPool )
        self.actionPool.triggered.connect( self.pool)
        # vytvorenie Pool used addresses
        self.actionPoolAddr = QAction( "Pool used addresses", self )
        self.menuPool.addAction( self.actionPoolAddr )
        self.actionPoolAddr.triggered.connect( self.poolUsed )
        # vytvorenie Route list
        self.actionRouteList = QAction( "Route list", self )
        self.menuRoute.addAction( self.actionRouteList )
        self.actionRouteList.triggered.connect( self.route )
        # vytvorenie Route nexthops
        self.actionRouteNExtHops = QAction( "RouteNext Hop", self )
        self.menuRoute.addAction( self.actionRouteNExtHops )
        self.actionRouteNExtHops.triggered.connect( self.nexthops )
        # vytvorenie Services
        self.actionServices = QAction( "Services IP", self )
        self.menuIP.addAction( self.actionServices )
        self.actionServices.triggered.connect( self.services)
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
        self.menuSystemInfo.addAction(self.actionDisks)
        self.actionDisks.triggered.connect(self.disks)
        #Driver
        self.actionDriver = QAction( "System driver", self )
        self.menuSystemInfo.addAction( self.actionDriver )
        self.actionDriver.triggered.connect( self.driver )
        #History
        self.actionHistory = QAction( "System history", self )
        self.menuSystemInfo.addAction( self.actionHistory )
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
        self.menuSystemInfo.addAction( self.actionIrq )
        self.actionIrq.triggered.connect( self.irq )
        #Resource CPU
        self.actionCpu = QAction( "CPU info", self )
        self.menuSystemInfo.addAction( self.actionCpu )
        self.actionCpu.triggered.connect( self.cpu )
        # Resource USB
        self.actionUsb = QAction( "USB info", self )
        self.menuSystemInfo.addAction( self.actionUsb )
        self.actionUsb.triggered.connect( self.usb)
        # Resource PCI
        self.actionPci = QAction( "PCI info", self )
        self.menuSystemInfo.addAction( self.actionPci)
        self.actionPci.triggered.connect( self.pci )
        #Users
        self.actionUsers = QAction( "System users", self )
        self.menuUser.addAction( self.actionUsers )
        self.actionUsers.triggered.connect( self.users )
        #Active users
        self.actionGroup = QAction( "Active users", self )
        self.menuUser.addAction( self.actionGroup )
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
        self.actionBridge.triggered.connect(self.bridge)
        #Bridge ports -canceling, not compatible with API
        #self.actionBridgePort = QAction( "Ports", self )
        #self.menuBridge.addAction( self.actionBridgePort )
        #self.actionBridgePort.triggered.connect( self.bridgePort )
        # Bridge VLAN
        self.actionBridgeVlan = QAction( "VLAN", self )
        self.menuBridge.addAction( self.actionBridgeVlan )
        self.actionBridgeVlan.triggered.connect( self.bridgeVlan )
        # Bridge connections
        self.actionBridgeConnections = QAction( "Connections", self )
        self.menuBridge.addAction( self.actionBridgeConnections )
        self.actionBridgeConnections.triggered.connect( self.bridgeHosts )
        # Wireless
        self.actionWifi = QAction( "Wifi interfaces", self )
        self.menuWireless.addAction( self.actionWifi )
        self.actionWifi.triggered.connect( self.wirelessInterface )
        # Wireless Security
        self.actionWifiSec = QAction( "WPA2 security", self )
        self.menuWireless.addAction( self.actionWifiSec )
        self.actionWifiSec.triggered.connect( self.security)
        # Wireless conenctions
        self.actionWifiCon = QAction( "Connection list", self )
        self.menuWireless.addAction( self.actionWifiCon )
        self.actionWifiCon.triggered.connect( self.registrationTable )

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
        print("C")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Info")
        self.msg.setInformativeText("Diploma thesis software")
        self.msg.setWindowTitle("About")
        self.msg.show()

    def reboot(self):
        api = tikapy.TikapySslClient(self.server,8729)
        api.login(self.user,self.pwd)
        api.talk(['/system/reboot'])
        sys.exit()

    def shutdown(self):
        api = tikapy.TikapySslClient( self.server,8729 )
        api.login( self.user, self.pwd )
        api.talk( ['/system/shutdown'] )
        sys.exit()

    def upgrade(self):
        try:
            api = tikapy.TikapySslClient( self.server,8729 )
            api.login( self.user, self.pwd )
            api.talk( ['/system/upgrade/download-all'] )
        except Exception as e:
            self.msg = QMessageBox()
            self.msg.setIcon( QMessageBox.Critical )
            self.msg.setText( "Connection error" )
            self.msg.setInformativeText( "Cannot reach server" )
            self.msg.setWindowTitle(str(e.args[0]))
            self.msg.show()

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

    def bridgeHosts(self):
        self.opened_window = bridgeConnections(self.user,self.pwd,self.server)
        self.opened_window.show()

    def bridgeVlan(self):
        self.opened_window = bridgeVLAN(self.user,self.pwd,self.server)
        self.opened_window.show()

    def bridgePort(self):
        self.opened_window = bridgePort(self.user,self.pwd,self.server)
        self.opened_window.show()

    def bridge(self):
        self.opened_window = bridgeGUI(self.user,self.pwd,self.server)
        self.opened_window.show()

    def wirelessInterface(self):
        self.opened_window = wirelessInterfaceGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def security(self):
        self.opened_window = securityGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def registrationTable(self):
        self.opened_window = registrationGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def services(self):
        self.opened_window = servicesGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def nexthops(self):
        self.opened_window= nextHopGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def poolUsed(self):
        self.opened_window = poolUsedGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def route(self):
        self.opened_window =routeGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def pool(self):
        self.opened_window = poolGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def neighbors(self):
        self.opened_window = neighborList(self.user,self.pwd,self.server)
        self.opened_window.show()

    def fwcon(self):
        self.opened_window = fwConnection(self.user,self.pwd,self.server)
        self.opened_window.show()

    def nat(self):
        self.opened_window = natGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def filter(self):
        self.opened_window = fwGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def serviceport(self):
        self.opened_window = servicePortGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def firewallConnection(self):
        pass

    def addressList(self):
        self.opened_window = addresslistGui(self.user,self.pwd,self.server)
        self.opened_window.show()

    def staticrecord(self):
        pass

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