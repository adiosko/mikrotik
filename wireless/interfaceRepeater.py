from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceRepeater:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setAddress(self,address):
        """

        :param address:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/setup-repeater','=address='+address])
        return wifi

    def setSsid(self,ssid):
        """

        :param ssid:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/setup-repeater', '=ssid=' + ssid] )
        return wifi

    def setPassphrase(self,password):
        """

        :param password:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/setup-repeater', '=passphrase=' + password] )
        return wifi

    