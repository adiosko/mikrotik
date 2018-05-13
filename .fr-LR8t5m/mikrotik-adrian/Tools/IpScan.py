from tikapy import TikapyClient
from tikapy import TikapySslClient

class IpScan:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def ScanAddressesOnInterface(self,interface,duration):
        """
        Method will list all IPs
        :param interface: interface on which we scan
        :param duration:  duration time f.e 5s
        :return: list
        """
        addresses = self.client.talk(['/tool/ip-scan','=interface='+interface,'=duration='+duration])
        return addresses

    def scan(self,duration):
        """
        Method will scan for some time
        :param duration: duration time
        :return:  list
        """
        addresses = self.client.talk(['/tool/ip-scan','=duration='+duration])
        return addresses

    def scanOnAddressRange(self,addressRange,duration):
        """
        Method will scan range addresses on subnet
        :param addressRange: address range
        :param duration: duration period
        :return:  list
        """
        addresses = self.client.talk(['/tool/ip-scan','=address-range='+addressRange,'=duration='+duration])
        return addresses