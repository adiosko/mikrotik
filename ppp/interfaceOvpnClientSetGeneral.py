from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceOvpnClientSetGeneral:
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
        ppp = self.client.talk(['/interface/ppp-client/set','=numbers='+name,'=name='+newName])
        return ppp

    def setMacAddress(self,name,mac):
        """
        Method will set name
        :param name:
        :param mac:
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/set','=numbers='+name,'=mac-address='+mac])
        return ppp

    def setMaxMtu(self,name,mtu="1500"):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/set','=numbers='+name,'=max-mtu='+mtu])
        return ppp