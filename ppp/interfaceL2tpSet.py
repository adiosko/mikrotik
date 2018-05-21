from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceL2tpServerSet:
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
        l2tp = self.client.talk(['/interface/l2tp-server/set','=numbers='+name,'=name='+newName])
        return l2tp

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        l2tp = self.client.talk( ['/interface/l2tp-server/set', '=numbers=' + name, '=user=' + user] )
        return l2tp

