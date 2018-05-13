from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficFlow:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable traffic flow
        :return:
        """
        flow = self.client.talk(['/ip/traffic-flow/set','=enabled=yes'])
        return flow

    def disable(self):
        """
        Method will disable traffic flow
        :return:
        """
        flow = self.client.talk( ['/ip/traffic-flow/set', '=enabled=no'] )
        return flow

    def setInterfaces(self,iface="all"):
        """
        Method will set traff flow iface
        :param iface:
        :return:
        """
        flow = self.client.talk( ['/ip/traffic-flow/set', '=interfaces='+iface] )
        return flow

    def cacheEntries(self,entry="16k"):
        """
        Method will cache entries
        :param entry: 1M, 2M, 4M,8M, 16M,32M,64k,256k,1k,2k,4k,8k,16k,32k,128k,512k
        :return:
        """
        flow = self.client.talk( ['/ip/traffic-flow/set', '=cache-entries=' + entry] )
        return flow

    def setActiveFloatTimeout(self,number,flow="00:30:00"):
        """
        Method will set float timeout
        :param number:
        :param flow:
        :return:
        """
        flow = self.client.talk( ['/ip/traffic-flow/set', '=active-float=timeout=' + flow] )
        return flow

    def setInActiveFloatTimeout(self,number,flow="00:30:00"):
        """
        Method will set float timeout
        :param number:
        :param flow:
        :return:
        """
        flow = self.client.talk( ['/ip/traffic-flow/set', '=inactive-float=timeout=' + flow] )
        return flow