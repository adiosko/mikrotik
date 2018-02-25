from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePptpClientSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setName(self,name,newName):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        pptp = self.client.talk(['/interface/pptp-client/set','=numbers='+name,'=name='+newName])
        return pptp

    def setMaxMtu(self,name,mtu="1450"):
        """
        Method will set max mtu
        :param name:
        :param mtu:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=max-mtu=' + mtu] )
        return pptp

    def setMaxMru(self,name,mru="1450"):
        """
        Method will set max mru
        :param name:
        :param mru:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=max-mru=' + mru] )
        return pptp

    def setMrru(self,name,mrru="1500"):
        """
        Method will set mrru
        :param name:
        :param mrru:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=mrru=' + mrru] )
        return pptp