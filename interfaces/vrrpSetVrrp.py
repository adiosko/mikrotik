from tikapy import TikapyClient
from tikapy import TikapySslClient


class vrrpSetVrrp:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setInterface(self,name,interface):
        """

        :param name:
        :param interface:
        :return:
        """
        vrrp = self.client.talk(['/interface/vrrp/set','=numbers='+name,'=interface='+interface])
        return vrrp

    def setVrid(self,name,ID="1"):
        """

        :param name:
        :param ID:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=vrid=' + ID] )
        return vrrp

    def setPriority(self,name,priority="100"):
        """

        :param name:
        :param priority:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=priority=' + priority] )
        return vrrp

    def setInterval(self,name,interval="100"):
        """

        :param name:
        :param interval:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=interval=' + interval] )
        return vrrp

    def enablePrrept(self,name):
        """

        :param name:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=preemption-mode=yes'] )
        return vrrp

    def disablePreempt(self,name):
        """

        :param name:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=preemption-mode=no'] )
        return vrrp

    def setAuthentication(self,name,auth="none"):
        """

        :param name:
        :param auth: none,simple,ah
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=authentication='+auth] )
        return vrrp

    def setPassword(self,name,password):
        """

        :param name:
        :param password:
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=password='+password] )
        return vrrp

    def setVersion(self,name,version="3"):
        """

        :param name:
        :param version:2,3
        :return:
        """
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=version='+version] )
        return vrrp

    def setV3Protocol(self,name,protocol):
        """

        :param name:
        :param protocol: ipv4,ipv6
        :return:
        """
        self.setVersion(name)
        vrrp = self.client.talk( ['/interface/vrrp/set', '=numbers=' + name, '=v3-protocol='+protocol] )
        return vrrp

