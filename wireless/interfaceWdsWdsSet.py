from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWdsWdsSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setMasterInterface(self,name,iface):
        """

        :param name:
        :param iface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=master-interface=' + iface] )
        return wifi

    def setWdsAddress(self,name,mac):
        """

        :param name:
        :param mac: 00:00:00:00:00:00 etc.
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/wds/set', '=numbers=' + name, '=wds-address=' + mac] )
        return wifi