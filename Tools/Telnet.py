from tikapy import TikapyClient
from tikapy import TikapySslClient

class Telnet:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def telnetHost(self,host):
        """
        Method will telnt to host
        :param host: host IP
        :return:
        """
        telnet = self.client.talk(['/system/telnet','=address='+host])
        return telnet

    def sshHost(self,address,user):
        """
        Method will log via ssh t remote server
        :param address: address of remote server
        :param user: user on remote server
        :return:
        """
        ssh = self.client.talk(['/system/ssh','=address='+address,'=user='+user])
        return ssh

    def macTelnetHost(self,host):
        """
        Method will login via amc address
        :param host: mac address of host
        :return: list
        """
        mac = self.client.talk(['/tool/mac-telnet','=host='+host])
        return mac
