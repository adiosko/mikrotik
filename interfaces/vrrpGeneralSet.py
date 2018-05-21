from tikapy import TikapyClient
from tikapy import TikapySslClient


class vrrpGeneralSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/set','=numbers='+name,'=name='+newName])
        return vrrp

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=mtu=' + mtu] )
        return vrrp

    def setArp(self,name,arp="enabled"):
        """

        :param name:
        :param arp: enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=arp=' + arp] )
        return vrrp

    def setArpTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=arp-timeout=' + timeout] )
        return vrrp