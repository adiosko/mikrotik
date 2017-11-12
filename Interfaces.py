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
            print( listinterfaces )  # vrati ether1
            print( listmacs )
        return interfaces


