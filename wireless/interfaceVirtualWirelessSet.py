from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceVirtualWirelessAllignmentOnlySet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setMode(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=mode=alignment-only'])
        return wifi

    def setSsid(self,name,ssid):
        """

        :param name:
        :param ssid:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=ssid='+ssid])
        return wifi

    def setMasterInterface(self,name,iface):
        """

        :param name:
        :param iface:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=master-interface='+iface])
        return wifi

    def setSecurityProfile(self,name,profile="default"):
        """

        :param name:
        :param profile:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=security-profile='+profile])
        return wifi

    def sedDefaultAuthentication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=default-authentication=yes'])
        return wifi

    def setNoDefaultAUthentication(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=default-authentication=no'])
        return wifi


