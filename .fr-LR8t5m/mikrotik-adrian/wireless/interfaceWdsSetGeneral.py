from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWdsSetGeneral:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wds/set','=numbers='+name,'=name='+newName])
        return wifi

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=mtu=' + mtu] )
        return wifi

    def setL2MTU(self,name,mtu="1600"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=l2mtu=' + mtu] )
        return wifi

    def setArp(self,name,arp="enabled"):
        """

        :param name:
        :param arp: enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=arp=' + arp] )
        return wifi

    def setArpTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=arp-timeout=' + timeout] )
        return wifi