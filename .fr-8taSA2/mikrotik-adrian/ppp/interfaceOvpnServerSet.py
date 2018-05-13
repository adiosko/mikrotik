from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceOvpnServerBinding:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)
        
    
    def setName(self,name,newName):
        """
        Method will rename iface
        :param name:
        :param newName:
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-server/set','=numbers='+name,'=name='+newName])
        return ovpn

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        ovpn = self.client.talk( ['/interface/ovpn-server/set', '=numbers=' + name, '=user=' + user] )
        return ovpn