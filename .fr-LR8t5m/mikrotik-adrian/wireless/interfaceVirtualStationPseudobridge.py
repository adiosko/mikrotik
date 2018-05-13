from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceVirtualStationPseudobridge:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setMode(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=mode=station-pseudobridge'] )
        return wifi

    def setSsid(self, name, ssid):
        """

        :param name:
        :param ssid:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=ssid=' + ssid] )
        return wifi

    def setMasterInterface(self, name, iface):
        """

        :param name:
        :param iface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=master-interface=' + iface] )
        return wifi

    def setSecurityProfile(self, name, profile="default"):
        """

        :param name:
        :param profile:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=security-profile=' + profile] )
        return wifi

    def setWmmSuport(self,name,support="disabled"):
        """

        :param name:
        :param support: disabled,enabled,required
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wmm-support=' + support] )
        return wifi

    def setMulticastHelper(self,name,helper="default"):
        """

        :param name:
        :param helper:  default, disabled, full
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-helper=' + helper] )
        return wifi

    def enableMulticastBuffering(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-buffering=yes'] )
        return wifi

    def disableMulticastBuffering(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=multicast-buffering=no'] )
        return wifi

    def enableKeepAliveFramers(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=keepalive-frames=yes'] )
        return wifi

    def disableKeepAliveFramers(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=keepalive-frames=no'] )
        return wifi

    def enableDefaultAuthenticate(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-authentication=yes'] )
        return wifi

    def disableDefaultAuthenticate(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=default-authentication=no'] )
        return wifi