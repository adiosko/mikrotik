from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceVirtual:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listInterfaces(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addAP(self,masteriFace,ssid,profile="default"):
        """
        :param masteriFace: wireless iface
        :param ssid:
        :param profile: default,
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/add','=mode=ap-bridge','=master-interface='+masteriFace,
                                 '=ssid='+ssid,'=security-profile='+profile])
        return wifi

    def addCLient(self,masteriFace,ssid,profile):
        """

        :param masteriFace:
        :param ssid:
        :param profile:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/add','=mode=station','=master-interface='+masteriFace,
                                 '=ssid='+ssid,'=security-profile='+profile])
        return wifi

    def removeInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/remove','=numbers='+name])
        return wifi

    def enableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/enable', '=numbers=' + name])
        return wifi

    def disableInterface(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/disable', '=numbers=' + name])
        return wifi

    def commentInterface(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/comment', '=numbers=' + name,'=comment='+comment])
        return wifi