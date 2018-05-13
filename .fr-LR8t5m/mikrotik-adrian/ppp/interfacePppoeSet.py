from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppoeServerSet:
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
        pppoe = self.client.talk(['/interface/pppoe-server/set','=numbers='+name,'=name='+newName])
        return pppoe

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-server/set', '=numbers=' + name, '=user=' + user] )
        return pppoe

    def setService(self,name,service):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-server/set', '=numbers=' + name, '=service=' + service] )
        return pppoe