from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppoeClientSetGeneral:
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
        pppoe = self.client.talk(['/interface/pppoe-client/set','=numbers='+name,'=name='+newName])
        return pppoe

    def setMaxMtu(self,name,mtu="1450"):
        """
        Method will set max mtu
        :param name:
        :param mtu:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=max-mtu=' + mtu] )
        return pppoe

    def setMaxMru(self,name,mru="1450"):
        """
        Method will set max mru
        :param name:
        :param mru:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=max-mru=' + mru] )
        return pppoe

    def setMrru(self,name,mrru="1500"):
        """
        Method will set mrru
        :param name:
        :param mrru:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=mrru=' + mrru] )
        return pppoe
    
    def setInterface(self,name,interface="ether1"):
        """
        Method will set mrru
        :param name:
        :param interface:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=interface=' + interface] )
        return pppoe