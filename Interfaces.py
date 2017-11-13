import LoginManager
from os import system
import pexpect
from tikapy import TikapyClient
from pprint import pprint

class InterfaceManager:
    def __init__(self,address):
        #self.interface = interface
        #self.mac = mac
        self.client  = TikapyClient(address,8728)

    def listInterfaces(self):
        """
        method which lists all interfaces on mikrotik
        :return: list of interfaces (optional mac addresses) on mikrotik
        """
        interfaces = {}
        self.client.login('admin','admin')
        interfaces = self.client.talk(['/interface/print'])
        for i in interfaces:
            listinterfaces = interfaces[i]['name']
            listmacs = interfaces[i]['mac-address']
            run = interfaces[i]['running']
            print( "Interface "+i+" name: "+listinterfaces)  # vrati ether1
            print( "Interface "+i+" MAC address: "+listmacs)
            print("Interface "+i+" is running: "+run)
            return interfaces

    def listEthernetInterfaces(self):
        """
        method will return all ethernet interfaces
        :return: list of ethernet interfaces
        """
        interfaces = {}
        self.client.login('admin','admin')
        interfaces = self.client.talk(['/interface/ethernet/print'])
        for i in interfaces:
            listethernet = interfaces[i]['name']
            print(listethernet)
        return interfaces

    def listEoIPInterfaces(self):
        """
        method will return all ethernet interfaces
        :return: list of ethernet interfaces
        """
        interfaces = {}
        self.client.login( 'admin', 'admin' )
        interfaces = self.client.talk( ['/interface/eoip/print'] )
        for i in interfaces:
            listeoip = interfaces[i]['name']
            if  listeoip:
                print(listeoip)
            else:
                print("No EoIP interface found")
        return interfaces

    def listBridgeInterfaces(self):
        """
        list all bridges on mikrotik
        :return: list of bridge interfaces
        """
        interfaces = {}
        self.client.login( 'admin', 'admin' )
        interfaces = self.client.talk(['/interface/bridge/print'])
        for i in interfaces:
            listbridge = interfaces[i]['name']
            bridgeports = self.client.talk(['/interface/bridge/port/print'])
            print("Available bridges are: "+listbridge)
        return interfaces

    def listVLANinterfaces(self):
        """
        return all VLAN interfaces
        :return:
        """
        interfaces = {}
        self.client.login( 'admin', 'admin' )
        interfaces = self.client.talk( ['/interface/eoip/print'] )
        for i in interfaces:
            listeoip = interfaces[i]['name']
            if listeoip:
                print( listeoip )
            else:
                print( "No EoIP interface found" )
        return interfaces
