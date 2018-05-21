from tikapy import TikapyClient
from tikapy import TikapySslClient

class Socks:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable socks
        :return:
        """
        socks = self.client.talk(['/ip/socks/set','=enabled=yes'])
        return socks

    def disable(self):
        """
        Method will disable socks
        :return:
        """
        socks = self.client.talk( ['/ip/socks/set', '=enabled=no'] )
        return socks

    def setPort(self,port="1080"):
        """
        Method will set port
        :param port:
        :return:
        """
        socks = self.client.talk(['/ip/socks/set','=port='+port])
        return socks

    def setIdleTimeout(self,timeout="00:02:00"):
        """
        Method will set connection idle timeout
        :param timeout:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/set', '=connection-idle-timeout=' + timeout] )
        return socks

    def setMaxConnections(self,maxim="200"):
        """
        Method will set max connection limit
        :param maxim:
        :return:
        """
        socks = self.client.talk( ['/ip/socks/set', '=max-connections=' + maxim] )
        return socks
