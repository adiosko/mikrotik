from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceL2tpClientSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setName(self,name,newName):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        l2tp = self.client.talk(['/interface/l2tp-client/set','=numbers='+name,'=name='+newName])
        return l2tp

    def setMaxMtu(self,name,mtu="1450"):
        """
        Method will set max mtu
        :param name:
        :param mtu:
        :return:
        """
        l2tp = self.client.talk( ['/interface/l2tp-client/set', '=numbers=' + name, '=max-mtu=' + mtu] )
        return l2tp

    def setMaxMru(self,name,mru="1450"):
        """
        Method will set max mru
        :param name:
        :param mru:
        :return:
        """
        l2tp = self.client.talk( ['/interface/l2tp-client/set', '=numbers=' + name, '=max-mru=' + mru] )
        return l2tp

    def setMrru(self,name,mrru="1500"):
        """
        Method will set mrru
        :param name:
        :param mrru:
        :return:
        """
        l2tp = self.client.talk( ['/interface/l2tp-client/set', '=numbers=' + name, '=mrru=' + mrru] )
        return l2tp