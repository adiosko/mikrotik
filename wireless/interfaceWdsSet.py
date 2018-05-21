from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWds:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setWdsMode(self,name,mode="disabled"):
        """

        :param name:
        :param mode: disabled, dynamic,dynamic-mesh,static,static-mesh
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/set','=numbers='+name,'=wds-mode='+mode])
        return wifi

    def setWdsDefaultBridge(self,name,bridge="none"):
        """

        :param name:
        :param bridge:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wds-default-bridge=' + bridge] )
        return wifi

    def setWdsDefaultCOst(self,name,cost="0"):
        """

        :param name:
        :param cost:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wds-default-cost=' + cost] )
        return wifi

    def setWdsCostRange(self,name,rangis="0"):
        """

        :param name:
        :param rangis:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wds-cost-range=' + rangis] )
        return wifi

    def enableWdsIgnorSsid(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wds-ignore-ssid=yes'] )
        return wifi

    def disableWdsIgnorSsid(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/set', '=numbers=' + name, '=wds-ignore-ssid=no'] )
        return wifi

