from tikapy import TikapyClient
from tikapy import TikapySslClient

class bridgeNatStp:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setType(self,number,stp="none"):
        """
        Method will set type of stp
        :param number:
        :param stp:config,tcn
        :return:
        """
        stp = self.client.talk(['/interface/bridge/filter/set','=numbers='+number,'=stp-type='+stp])
        return stp

    def setFlags(self, number, stp="0"):
        """
        Method will set type of stp
        :param number:
        :param stp:config,tcn
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-flags=' + stp] )
        return stp

    def setArpRootAddress(self, number, mac, mask):
        """
        Method will set arp hw type
        :param number:
        :param mac:
        :return:
        """
        arp = self.client.talk(
            ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-root-address=' + mac + "/" + mask] )
        return arp

    def setRootCost(self,number,cost="0-4294967295"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-root-cost=' + cost] )
        return stp

    def setStpSenderAddress(self, number, mac, mask):
        """
        Method will set arp hw type
        :param number:
        :param mac:
        :return:
        """
        arp = self.client.talk(
            ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-sender-address=' + mac + "/" + mask] )
        return arp

    def setStpPort(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-port=' + cost] )
        return stp

    def setStpRootPriority(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-root-priority=' + cost] )
        return stp

    def setStpSenderPriority(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-sender-priority=' + cost] )
        return stp

    def setStpMsgAge(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-msg-age=' + cost] )
        return stp

    def setStpMaxAge(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-max-age=' + cost] )
        return stp

    def setStpHelloInterval(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-hello-time=' + cost] )
        return stp

    def setStpForwardDelay(self, number, cost="0-65535"):
        """
        Method wil lset root cost
        :param number:
        :param cost:
        :return:
        """
        stp = self.client.talk( ['/interface/bridge/filter/set', '=numbers=' + number, '=stp-forward-delay=' + cost] )
        return stp


