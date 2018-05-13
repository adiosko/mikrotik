from tikapy import TikapyClient
from tikapy import TikapySslClient


class vlanSetGeneral:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )
        
    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        iface = self.client.talk(['/interface/vlan/set','=numbers='+name,'=name='+newName])
        return iface

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        iface = self.client.talk(['/interface/vlan/set', '=numbers=' + name, '=mtu=' + mtu])
        return iface

    def setArp(self,name,arp="enabled"):
        """

        :param name:
        :param arp:enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        iface = self.client.talk(['/interface/vlan/set', '=numbers=' + name, '=arp=' + arp])
        return iface

    def setArpTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        iface = self.client.talk(['/interface/vlan/set', '=numbers=' + name, '=arp-timeout=' + timeout])
        return iface

    def setVlanId(self,name,vlanId="1"):
        """

        :param name:
        :param vlanId:
        :return:
        """
        iface = self.client.talk(['/interface/vlan/set','=numbers='+name,'=vlan-id='+vlanId])
        return iface

    def setVlanInterface(self,name,interface):
        """

        :param name:
        :param interface:
        :return:
        """
        iface = self.client.talk( ['/interface/vlan/set', '=numbers=' + name, '=interface=' + interface] )
        return iface

    def useServiceTag(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/vlan/set', '=numbers=' + name, '=use-service-tag=yes'] )
        return iface

    def notUseServiceTag(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/vlan/set', '=numbers=' + name, '=use-service-tag=no'] )
        return iface