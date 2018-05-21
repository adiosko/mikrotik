from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePptpServerSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setName(self,name,newName):
        """
        Method will rename iface
        :param name:
        :param newName:
        :return:
        """
        pptp = self.client.talk(['/interface/pptp-server/set','=numbers='+name,'=name='+newName])
        return pptp

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-server/set', '=numbers=' + name, '=user=' + user] )
        return pptp