from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWpsCLient:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setSsid(self,ssid):
        """

        :param ssid:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/wps-client','=ssid='+ssid])
        return wifi

    def setMacAddress(self,mac):
        """

        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wps-client', '=mac-address=' + mac] )
        return wifi

    def createProfile(self,profile="wps-profile"):
        """

        :param profile:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wps-client', '=create-profile=' + profile] )
        return wifi