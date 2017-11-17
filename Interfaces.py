import LoginManager
from os import system
import pexpect
from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class InterfaceManager:
    def __init__(self,address,username,password):
        self.client  = TikapyClient(address,8728)
        self.client.login( username, password)

    def listInterfaces(self):
        """
        method which lists all interfaces on mikrotik
        :return: list of interfaces (optional mac addresses) on mikrotik
        """
        interfaces = {}

        interfaces = self.client.talk(['/interface/print'])
        print("Interfaces on mikrotik are: ")
        for i in interfaces:
            listinterfaces = interfaces[i]['name']
            listmacs = interfaces[i]['mac-address']
            run = interfaces[i]['running']
            disabled = interfaces[i]['disabled']
            #print(listinterfaces)
            print(listinterfaces)
        return interfaces

    def listEthernetInterfaces(self):
        """
        method will return all ethernet interfaces
        :return: list of ethernet interfaces
        """
        interfaces = {}
        interfaces = self.client.talk(['/interface/ethernet/print'])
        for i in interfaces:
            listethernet = interfaces[i]['name']
            print(listethernet)
            print(interfaces)
        return interfaces

    def listEoIPInterfaces(self):
        """
        method will return all ethernet interfaces
        :return: list of ethernet interfaces
        """
        interfaces = {}
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
        interfaces = self.client.talk( ['/interface/vlan/print'] )
        for i in interfaces:
            listvlan = interfaces[i]['name']
            if listvlan:
                print(listvlan)
            else:
                print( "No EoIP interface found" )
        return interfaces
