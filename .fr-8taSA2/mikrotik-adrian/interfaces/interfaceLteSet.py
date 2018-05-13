from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacesLteSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def allowRoaming(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set','=numbers='+name,'=allow-roaming=yes'])
        return iface

    def notAllowRoaming(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=allow-roaming=no'])
        return iface

    def setApnProfile(self,name,profile):
        """

        :param name:
        :param profile: default or custom
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=apn-profiles='+profile])
        return iface

    def setBand(self,name,band):
        """

        :param name:
        :param band:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=band='+band])
        return iface

    def setMacAddress(self,name,mac):
        """

        :param name:
        :param mac:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=mac-address='+mac])
        return iface

    def setModemInit(self,name,modem):
        """

        :param name:
        :param modem:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=modem-init='+modem])
        return iface

    def setMtu(self,name,mtu="1500"):
        """

        :param name:
        :param mtu:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=mtu='+mtu])
        return iface

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=name='+newName])
        return iface

    def setNetworkMode(self,name,mode="3g"):
        """

        :param name:
        :param mode:3g,gsm,lte
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=network-mode='+mode])
        return iface

    def setPin(self,name,pin):
        """

        :param name:
        :param pin:
        :return:
        """
        iface = self.client.talk(['/interface/lte/set', '=numbers=' + name, '=pin='+pin])
        return iface