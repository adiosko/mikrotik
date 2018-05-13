from tikapy import TikapyClient
from tikapy import TikapySslClient

class Ping:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def pingToAddress(self,address,count):
        """
        Method will ping to specific address
        :param address: address to reach
        :param count: count of packets
        :return:
        """
        ping = self.client.talk(['/ping','=address='+address,'=count='+count])
        print(ping)
        return ping

    def pingWithSpecificInterface(self,dst,interface,count):
        """
        Method will ping dst with specific interface
        :param dst: dst address
        :param interface: intreface
        :param count: count of packets
        :return:
        """
        ping = self.client.talk(['/ping','address='+dst,'=interface='+interface,'=count='+count])
        print(ping)
        return ping

    def enableArpPing(self,address):
        """
        Method will enable arp ping
        :param dst: address to ping
        :param count: count of packets
        :return:
        """
        ping = self.client.talk(['/ping','=arp-ping=yes','=address='+address])
        return ping

    def pingWithSourceAddress(self,dst,src,count):
        """
        Method will ping dst with src address
        :param dst: dst address
        :param src: src address
        :param count count of pings
        :return:
        """
        ping = self.client.talk(['/ping','=address='+dst,'=src-address='+src,'=count='+count])
        return ping