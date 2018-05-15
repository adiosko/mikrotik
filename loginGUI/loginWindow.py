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
from loginGUI.dnsGui import dnsGui
from loginGUI.ndsstaticGui import dnsstaticGui
from loginGUI.dnscacheGui import dnscacheGui
from loginGUI.dhcpleasesGui import dhcpleaseGui
from loginGUI.dhcpClientGui import dhcpClientGui
from loginGUI.dhcpRelayGui import dhcpRelayGui
from loginGUI.dhcpServerGui import dhcpServerGui
from loginGUI.interfaceListGui import interfaceListGui
from loginGUI.interfaceListMembers import interfaceListMemberGui
from loginGUI.ethernetGui import ethernetGui
from loginGUI.interfaceVlanGui import interfaceVlanGui
from loginGUI.mangleGui import mangleGui
from loginGUI.loggingGui import loggingGui
qtCreatorFile = "./loginGUI/loginWIndow.ui"

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
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.setWindowTitle( user + "@" + server )
        self.opened_window = []
        self.init_buttons()
        #sablona mikrotik tlacitka a menu (vytvorenie IP tlacitka)
        self.menu = self.menuBar()
        #velke menu
        self.menuInterface = self.menu.addMenu("Interface")
        self.menuIP = self.menu.addMenu("IP")
        self.menuPool = self.menu.addMenu( "Address pools" )
        self.menuBridge = self.menu.addMenu( "Bridge" )
        self.menuRoute = self.menu.addMenu( "Routing management" )
        self.menuDhcp = self.menu.addMenu("DHCP")
        self.menuDns = self.menu.addMenu( "DNS" )
        self.menuSystem = self.menu.addMenu( "Hostname" )
        self.menuFirewall = self.menu.addMenu( "Firewall" )
        self.menuWireless = self.menu.addMenu( "Wireless" )
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
        self.actionVLAN.triggered.connect( self.vlanInterface )
        #Connections
        self.actionIfaceCon = QAction( "Interface list members", self )
        self.menuInterface.addAction( self.actionIfaceCon )
        self.actionIfaceCon.triggered.connect( self. interfaceList)
        # Connections
        self.actionIfaceList = QAction( "Interface lists", self )
        self.menuInterface.addAction( self.actionIfaceList )
        self.actionIfaceList.triggered.connect( self.interfaceMembers )
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
        self.actionArp = QAction("ARP",self)
        self.menuIP.addAction( self.actionArp )
        self.actionArp.triggered.connect( self.openArpWindow)
        #vytvorenie DHCP klient
        self.actionDhcpClient = QAction("DHCP Client",self)
        self.menuDhcp.addAction(self.actionDhcpClient)
        self.actionDhcpClient.triggered.connect(self.dhcpclient)
        #dhcp relay
        self.actionRelay = QAction("DHCP Relay",self)
        self.menuDhcp.addAction(self.actionRelay)
        self.actionRelay.triggered.connect(self.dhcprelay)
        # vytvorenie DHCP server
        self.actionDhcpServer = QAction( "DHCP Server", self )
        self.menuDhcp.addAction( self.actionDhcpServer )
        self.actionDhcpServer.triggered.connect( self.dhcpserver )
        # vytvorenie DHCP server leases
        self.actionDhcpServerLeases = QAction( "DHCP Assigned Addresses", self )
        self.menuDhcp.addAction( self.actionDhcpServerLeases )
        self.actionDhcpServerLeases.triggered.connect( self.dhcplease )
        #DNS
        self.actionDNS = QAction("Add server",self)
        self.menuDns.addAction(self.actionDNS)
        self.actionDNS.triggered.connect(self.dnsServer)
        #DNS static record
        self.actionDNSStatic = QAction( "Static records", self )
        self.menuDns.addAction( self.actionDNSStatic )
        self.actionDNSStatic.triggered.connect( self.staticrecord )
        #DNS cache
        self.actionDNSCache = QAction("DNS chache",self)
        self.menuDns.addAction(self.actionDNSCache)
        self.actionDNSCache.triggered.connect(self.cachedns)
        # vytvorenie Filter rules
        self.actionFilter = QAction( "Filter rules", self )
        self.menuFirewall.addAction( self.actionFilter )
        self.actionFilter.triggered.connect( self.filter )
        # vytvorenie Filter rules
        self.actionNat = QAction( "NAT rules", self )
        self.menuFirewall.addAction( self.actionNat )
        self.actionNat.triggered.connect( self.nat )
        #vytvorenie mangle
        self.actionmangle = QAction("Mangle rules",self)
        self.menuFirewall.addAction(self.actionmangle)
        self.actionmangle.triggered.connect(self.mangle)
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
        #logging
        self.actionlogging = QAction("Logging", self)
        self.menuLog.addAction(self.actionlogging)
        self.actionlogging.triggered.connect(self.logging)
        #restore
        self.actionRestore = QAction("Restore configuration",self)
        self.menuMaintenance.addAction(self.actionRestore)
        self.actionRestore.triggered.connect(self.restore)
        #Bridge global
        self.actionBridge = QAction("Bridge",self)
        self.menuBridge.addAction(self.actionBridge)
        self.actionBridge.triggered.connect(self.bridge)
        #Bridge
        self.actionBridgePort = QAction( "Ports", self )
        self.menuBridge.addAction( self.actionBridgePort )
        self.actionBridgePort.triggered.connect( self.bridgePort )
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
        action = ipAddressesGui( self.user, self.pwd, self.server)
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(525,318)
        action.show()
        self.mdi.cascadeSubWindows()

    def openArpWindow(self):
        action = arpGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(625,298)
        action.show()
        self.mdi.cascadeSubWindows()

    def quit(self):
        sys.exit()

    def about(self):
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
        action = packages( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(353,396)
        action.show()
        self.mdi.cascadeSubWindows()

    def disks(self):
        action = disks( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(564,286)
        action.show()
        self.mdi.cascadeSubWindows()

    def driver(self):
        action = drivers( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(246,208)
        action.show()
        self.mdi.cascadeSubWindows()

    def files(self):
        action = fileGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.show()
        self.mdi.cascadeSubWindows()

    def history(self):
        action = history( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(858,464)
        action.show()
        self.mdi.cascadeSubWindows()

    def log(self):
        action = logGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(878,475)
        action.show()
        self.mdi.cascadeSubWindows()

    def restore(self):
        action = restoreGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(336,100)
        action.show()
        self.mdi.cascadeSubWindows()

    def identity(self):
        action = hostnameGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(402,90)
        action.show()
        self.mdi.cascadeSubWindows()

    def reset(self):
        action = resetGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(273,185)
        action.show()
        self.mdi.cascadeSubWindows()

    def irq(self):
        action = irqGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(743,284)
        action.show()
        self.mdi.cascadeSubWindows()

    def cpu(self):
        action = cpuGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(720,298)
        action.show()
        self.mdi.cascadeSubWindows()

    def usb(self):
        action = usbGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(750,243)
        action.show()
        self.mdi.cascadeSubWindows()

    def pci(self):
        action = pciGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(617,236)
        action.show()
        self.mdi.cascadeSubWindows()

    def listUsers(self):
        action = usersActive( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(844,265)
        action.show()
        self.mdi.cascadeSubWindows()

    def users(self):
        action = usersGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(684,299)
        action.show()
        self.mdi.cascadeSubWindows()

    def interfaces(self):
        action = interfaceGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize( 1101, 651)
        action.show()
        self.mdi.cascadeSubWindows()


    def bridgeHosts(self):
        action = bridgeConnections( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(782,289)
        action.show()
        self.mdi.cascadeSubWindows()

    def bridgeVlan(self):
        action = bridgeVLAN( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(657,263)
        action.show()
        self.mdi.cascadeSubWindows()

    def bridgePort(self):
        action = bridgePort( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1002,382)
        action.show()
        self.mdi.cascadeSubWindows()

    def bridge(self):
        action = bridgeGUI( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1042,248)
        action.show()
        self.mdi.cascadeSubWindows()

    def wirelessInterface(self):
        action = wirelessInterfaceGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(889,268)
        action.show()
        self.mdi.cascadeSubWindows()

    def security(self):
        action = securityGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(686,276)
        action.show()
        self.mdi.cascadeSubWindows()

    def registrationTable(self):
        action = registrationGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(637,263)
        action.show()
        self.mdi.cascadeSubWindows()

    def services(self):
        action = servicesGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(812,323)
        action.show()
        self.mdi.cascadeSubWindows()

    def nexthops(self):
        action = nextHopGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(702,282)
        action.show()
        self.mdi.cascadeSubWindows()

    def poolUsed(self):
        action = poolUsedGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(809,274)
        action.show()
        self.mdi.cascadeSubWindows()

    def route(self):
        action = routeGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(979,275)
        action.show()
        self.mdi.cascadeSubWindows()

    def pool(self):
        action = poolGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(457,245)
        action.show()
        self.mdi.cascadeSubWindows()

    def neighbors(self):
        action = neighborList( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(1122,301)
        action.show()
        self.mdi.cascadeSubWindows()

    def fwcon(self):
        action = fwConnection( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(952,405)
        action.show()
        self.mdi.cascadeSubWindows()

    def nat(self):
        action = natGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1278,626)
        action.show()
        self.mdi.cascadeSubWindows()

    def filter(self):
        action = fwGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1449,595)
        action.show()
        self.mdi.cascadeSubWindows()

    def serviceport(self):
        action = servicePortGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(725,342)
        action.show()
        self.mdi.cascadeSubWindows()

    def dnsServer(self):
        action = dnsGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(426,111)
        action.show()
        self.mdi.cascadeSubWindows()

    def firewallConnection(self):
        pass

    def addressList(self):
        action = addresslistGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(991,357)
        action.show()
        self.mdi.cascadeSubWindows()

    def cachedns(self):
        action = dnscacheGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(647,365)
        action.show()
        self.mdi.cascadeSubWindows()

    def staticrecord(self):
        action = dnsstaticGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(745,356)
        action.show()
        self.mdi.cascadeSubWindows()

    def dhcplease(self):
        action = dhcpleaseGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(1030,391)
        action.show()
        self.mdi.cascadeSubWindows()

    def dhcpclient(self):
        action = dhcpClientGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1086,415)
        action.show()
        self.mdi.cascadeSubWindows()

    def dhcprelay(self):
        action = dhcpRelayGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(815,374)
        action.show()
        self.mdi.cascadeSubWindows()

    def dhcpserver(self):
        action = dhcpServerGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(946,341)
        action.show()
        self.mdi.cascadeSubWindows()

    def ethernet(self):
        action = ethernetGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(1239,339)
        action.show()
        self.mdi.cascadeSubWindows()

    def interfaceList(self):
        action = interfaceListGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(636,336)
        action.show()
        self.mdi.cascadeSubWindows()

    def interfaceMembers(self):
        action = interfaceListMemberGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(715,352)
        action.show()
        self.mdi.cascadeSubWindows()


    def vlanInterface(self):
        action = interfaceVlanGui( self.user, self.pwd, self.server )
        action.parent = self
        self.mdi.addSubWindow( action )
        action.setFixedSize(1002,616)
        action.show()
        self.mdi.cascadeSubWindows()

    def mangle(self):
        mangle = mangleGui(self.user,self.pwd,self.server)
        mangle.parent = self
        self.mdi.addSubWindow(mangle)
        mangle.setFixedSize(1282,646)
        mangle.show()
        self.mdi.cascadeSubWindows()

    def logging(self):
        action = loggingGui( self.user, self.pwd, self.server )
        self.mdi.addSubWindow( action )
        action.setFixedSize(1081,462)
        action.show()
        self.mdi.cascadeSubWindows()

if __name__ == "__main__":
    app = QtGui.QApplication( sys.argv )
    window = loginMikrotik()
    window.show()
    sys.exit( app.exec_() )