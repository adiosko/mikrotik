import LoginManager
import apiList
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
        interfaces = {}
        self.client.login('admin','admin')
        interfaces = self.client.talk(['/interface/print'])
        #print(interfaces)
        return interfaces


