from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/set','=numbers='+name,'=name='+newName])
        return wifi

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=mtu=' + mtu] )
        return wifi

    def setMacAddress(self,name,mac="00:00:00:00:00:00"):
        """

        :param name:
        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=mac-address=' + mac] )
        return wifi

    def setArp(self,name,arp="enabled"):
        """

        :param name:
        :param arp: enabled,disabled,local-proxy-arp,proxy-arp,none
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=arp=' + arp] )
        return wifi

    def setArpTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=arp-timeout=' + timeout] )
        return wifi

    def setRadioMac(self,name,mac="00:00:00:00:00:00"):
        """

        :param name:
        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=radio-mac=' + mac] )
        return wifi

    def setMasterInterface(self,name,master="none"):
        """

        :param name:
        :param master:  none or cap iface
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=master-interface=' + master] )
        return wifi