from tikapy import TikapyClient
from tikapy import TikapySslClient

class DNSglobal:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setServers(self,server):
        """
        Method will set dns servers
        :param server:
        :return:
        """
        dns = self.client.talk(['/ip/dns/set','=servers='+server,'=allow-remote-requests=yes'])
        return dns

    def allowRemoteRequests(self,rq="yes"):
        """
        Method will set remote peers for dns (domain f.e)
        :param rq:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=allow-remote-requests='+rq] )
        return dns

    def setMaxUdpDatagram(self,maxim="4096"):
        """
        Method will set max datagram
        :param maxim:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=max-udp-packet-size=' + maxim] )
        return dns

    def setQueryServerTimeout(self,time="2000"):
        """
        Method will set timeout
        :param time: in secs
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=query-server-timeout=' + time] )
        return dns

    def setQueryTotalTimeout(self,time="10000"):
        """
        Method will set total timeout
        :param time:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=query-total-timeout=' + time] )
        return dns

    def setCacheSize(self,casize="2048"):
        """
        Method will set cache buffer size
        :param casize: in kB
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=cache-size=' + casize] )
        return dns

    def setCacheMaxTtl(self,ttl="7d 00:00:00"):
        """
        Method will set max ttl
        :param ttl:
        :return:
        """
        dns = self.client.talk( ['/ip/dns/set', '=cache-max-ttl=' + ttl] )
        return dns