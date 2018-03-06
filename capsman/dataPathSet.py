from tikapy import TikapyClient
from tikapy import TikapySslClient

class DataPathSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=name=' + newName] )
        return wifi

    def setMtu(self,name,mtu="32"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=mtu=' + mtu] )
        return wifi

    def setL2Mtu(self,name,mtu="0"):
        """

        :param name:
        :param mtu:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=l2mtu=' + mtu] )
        return wifi

    def setArp(self,name,arp="disabled"):
        """

        :param name:
        :param arp: disabled,enabled,local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=arp=' + arp] )
        return wifi

    def setBridge(self,name,bridge):
        """

        :param name:
        :param bridge:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=bridge=' + bridge] )
        return wifi

    def setBridgeCost(self,name,cost="0"):
        """

        :param name:
        :param cost:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=bridge-cost=' + cost] )
        return wifi

    def setBridgeHorizon(self,name,horizon="0"):
        """

        :param name:
        :param horizon:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=bridge-horizon=' + horizon] )
        return wifi

    def setLocalForwarding(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=local-forwarding=yes'] )
        return wifi

    def unsetLocalForwarding(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=local-forwarding=no'] )
        return wifi

    def setClient2ClientCOmmunication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=client-to-client-forwarding=yes'] )
        return wifi

    def unsetClient2ClientCOmmunication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=client-to-client-forwarding=no'] )
        return wifi

    def setVlanMode(self,name,vlan="no-tag"):
        """

        :param name:
        :param vlan:  no-tag,use-service-tag, use-tag
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=vlan-mode='+vlan] )
        return wifi

    def setVladId(self,name,vlan="1"):
        """

        :param name:
        :param vlan:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/datapath/set', '=numbers=' + name, '=vlan-id='+vlan] )
        return wifi