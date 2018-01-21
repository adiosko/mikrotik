from tikapy import TikapyClient
from tikapy import TikapySslClient

class Settings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setIpv6Forward(self):
        """
        Method will set ipv6 forward
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/settings/set','=forward=yes'])
        return ipv6

    def  setAcceptRedirects(self,number):
        """
        Method will accept redirection
        :param number:
        :return:
        """
        ipv6 = self.client.talk(['/ipv6/settings/set','=accept-redirects=yes'])
        return ipv6

    def setAcceotRouterAdvertisements(self,adv="yes-if-forwarding-disabled"):
        """
        Method will set router advertisements
        :param adv: yes, no, yes-if-forwarding-disabled
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/settings/set', '=accept-router-advertisements='+adv] )
        return ipv6

    def setMaxNeighborEntries(self,entries="8192"):
        """
        Method will set neighbor max entries
        :param entries:
        :return:
        """
        ipv6 = self.client.talk( ['/ipv6/settings/set', '=entries=' + entries] )
        return ipv6