from tikapy import TikapyClient
from tikapy import TikapySslClient

class Settings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setIpForward(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk(['/ip/settings/set','=ip-forward=yes'])
        return settings

    def setSendRedirects(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=send-redirects=yes'] )
        return settings

    def setAcceptRedirects(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=accept-redirects=yes'] )
        return settings

    def setSecureRedirects(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=secure-redirects=yes'] )
        return settings

    def setAcceptSourceRoute(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=accept-source-route=yes'] )
        return settings

    def setAllowFastPath(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=allow-fast-path=yes'] )
        return settings

    def setRouteCache(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=route-cache=yes'] )
        return settings

    def setRpFilter(self,rp="no"):
        """
        method will set rd filter
        :param rp: loose, no, strict
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=rp-filter='+rp] )
        return settings

    def setTcpSynCookies(self):
        """
        Method will set ip forward
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=tcp-syncookies=yes'] )
        return settings

    def setMaxNeighborEntries(self,entries="8192"):
        """
        Method will set max neighbor entries
        :param entries:
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=max-neighbor-entries='+entries] )
        return settings

    def setArpTimeout(self,time="00:00:30"):
        """
        Method will set arp timeout
        :param time:
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=arp-timeout=' + time] )
        return settings

    def setIcmprateLimit(self,limit="10"):
        """
        Method will set icmp rate limit
        :param limit:
        :return:
        """
        settings = self.client.talk( ['/ip/settings/set', '=icmp-rate-limit=' + limit] )
        return settings