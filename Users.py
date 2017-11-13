import LoginManager
from os import system
import pexpect
from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class Users:
    def __init__(self,address):
        self.client = TikapyClient( address, 8728 )

    def listSystemUsers(self):
        users = {}
