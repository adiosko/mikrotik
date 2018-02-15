from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgeSettings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setUseIpFirewall(self):
        """
        Method will enable ip firewall
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/settings/set','=use-ip-firewall=yes'])
        return bridge

    def setUseIpFirewallVlan(self):
        """

        :return:
        """
        self.setUseIpFirewall()
        bridge = self.client.talk( ['/interface/bridge/settings/set', '=use-ip-firewall-for-vlan=yes'] )
        return bridge

    def setUseIpFirewallForPPPoE(self):
        """

        :return:
        """
        self.setUseIpFirewall()
        bridge = self.client.talk( ['/interface/bridge/settings/set', '=use-ip-firewall-for-pppoe=yes'] )
        return bridge

    def setAllowFastPath(self):
        """
        Method will enable fast path by default
        :return:
        """
        bridge = self.client.talk( ['/interface/bridge/settings/set', '=allow-fast-path=yes'] )
        return bridge