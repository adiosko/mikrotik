from tikapy import TikapyClient
from tikapy import TikapySslClient


class greTunelSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setName(self,name,newName):
        """
        :param name:
        :param newName:
        :return:
        """
        iface = self.client.talk(['/interface/gre/set','=numbers='+name,'=name='+newName])
        return iface

    def setMtu(self,name,mtu="64"):
        """
        :param name:
        :param mtu:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=mtu=' + mtu] )
        return iface

    def setLocalAddress(self,name,locAddress):
        """

        :param name:
        :param locAddress:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=local-address=' + locAddress] )
        return iface

    def setRemoteAddress(self,name,remoteAddress="0.0.0.0"):
        """

        :param name:
        :param remoteAddress:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=remote-address=' + remoteAddress] )
        return iface

    def setIpsecSecret(self,name,secret):
        """

        :param name:
        :param secret:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=ipsec-secret=' + secret] )
        return iface

    def setKeepAlive(self,name,keepalive="10s,10"):
        """

        :param name:
        :param keepalive:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=keepalive=' + keepalive] )
        return iface

    def setDscp(self,name,dscp="inherit"):
        """

        :param name:
        :param dscp: inherit
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=dscp=' + dscp] )
        return iface

    def setDontFragment(self,name,fragment="no"):
        """

        :param name:
        :param fragment:no,inherit
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=dont-fragment=' + fragment] )
        return iface

    def enableClampMssTcp(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=clamp-tcp-mss=yes'] )
        return iface

    def disableClampMss(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=clamp-tcp=mss=no'] )
        return iface

    def enableAllowFastPath(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=allow-fast-path=yes'] )
        return iface

    def disableAllowFastPath(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk( ['/interface/gre/set', '=numbers=' + name, '=allow-fast-path=no'] )
        return iface