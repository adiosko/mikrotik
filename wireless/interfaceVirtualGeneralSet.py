from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceVirtualGeneralSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=name='+newName])
        return wifi

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set', '=numbers=' + name, '=mtu=' + mtu])
        return wifi

    def setL2Mtu(self,name,l2mtu="1600"):
        """

        :param name:
        :param l2mtu:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set', '=numbers=' + name, '=l2mtu=' + l2mtu])
        return wifi

    def setMacAddress(self,name,mac="00:00:00:00:00:00"):
        """

        :param name:
        :param mac:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set', '=numbers=' + name, '=mac-address=' + mac])
        return wifi

    def setArp(self,name,arp="enabled"):
        """

        :param name:
        :param arp: enabled,disabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set', '=numbers=' + name, '=arp=' + arp])
        return wifi

    def setArpTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set', '=numbers=' + name, '=arp-timeout=' + timeout])
        return wifi

