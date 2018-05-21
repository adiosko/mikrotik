from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceDatapathSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setDataPathProfile(self,name,profile):
        """

        :param name:
        :param profile:
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/set','=numbers='+name,'=datapath='+profile])
        return wifi
    
    def setMtu(self,name,mtu="32"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.mtu=' + mtu] )
        return wifi

    def setL2Mtu(self,name,mtu="0"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.l2mtu=' + mtu] )
        return wifi

    def setArp(self,name,arp="disabled"):
        """

        :param name:
        :param arp: disabled,enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.arp=' + arp] )
        return wifi

    def setBridge(self,name,bridge):
        """

        :param name:
        :param bridge:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.bridge=' + bridge] )
        return wifi

    def setBridgeCost(self,name,cost="0"):
        """

        :param name:
        :param cost:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.bridge-cost=' + cost] )
        return wifi

    def setBridgeHorizon(self,name,horizon="0"):
        """

        :param name:
        :param horizon:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.bridge-horizon=' + horizon] )
        return wifi

    def setLocalForwarding(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.local-forwarding=yes'] )
        return wifi

    def unsetLocalForwarding(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.local-forwarding=no'] )
        return wifi

    def setClient2ClientCOmmunication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.client-to-client-forwarding=yes'] )
        return wifi

    def unsetClient2ClientCOmmunication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.client-to-client-forwarding=no'] )
        return wifi

    def setVlanMode(self,name,vlan="no-tag"):
        """

        :param name:
        :param vlan:  no-tag,use-service-tag, use-tag
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.vlan-mode='+vlan] )
        return wifi

    def setVladId(self,name,vlan="1"):
        """

        :param name:
        :param vlan:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=datapath.vlan-id='+vlan] )
        return wifi