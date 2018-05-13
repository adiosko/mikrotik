from tikapy import TikapyClient
from tikapy import TikapySslClient

class FirewallServicePOrts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPorts(self):
        """
        Method will list service ports
        :return:
        """
        ip = self.client.talk(['/ip/firewall/service-port/print'])
        return ip

    def enablePort(self,name):
        """
        Method will enable port
        :param name: name of service
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/service-port/enable','=numbers='+name] )
        return ip

    def disablePort(self,name):
        """
        Method will disable port
        :param number:
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/service-port/disable', '=numbers=' + name] )
        return ip

    def setPort(self,name,port):
        """
        Method will set port
        :param name:
        :param port:
        :return:
        """
        ip = self.client.talk(['/ip/firewall/service-port/set','=numbers='+name,'=ports='+port])
        return ip

    def setSipDirectMedia(self):
        """
        Method will set sip direct media
        :return:
        """
        ip = self.client.talk(['/ip/firewall/service-port/set','=numbers=sip','=sip-direct-media=yes'])
        return ip

    def unsetSipDirectMedia(self):
        """
        Method will set sip direct media
        :return:
        """
        ip = self.client.talk( ['/ip/firewall/service-port/set', '=numbers=sip', '=sip-direct-media=no'] )
        return ip

