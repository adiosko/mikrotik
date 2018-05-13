from tikapy import TikapyClient
from tikapy import TikapySslClient

class lteApnSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set','=numbers='+name,'=name='+newName])
        return iface

    def setApnName(self,name,apnName):
        """

        :param name:
        :param apnName:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=apn=' + apnName])
        return iface

    def setIpType(self,name,iptype="ipv4"):
        """

        :param name:
        :param iptype: ipv4,ipv4-ipv6,ipv6
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=ip-type=' + iptype])
        return iface

    def usePeerDns(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=use-peer-dns=yes'])
        return iface

    def notUsePeerDns(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set','=numbers='+name,'=use-peer-dns=no'])
        return iface

    def addDefaultRoute(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=add-default-route=yes'])
        return iface

    def notAddDefaultRoute(self,name):
        """

        :param name:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=add-default-route=no'])
        return iface

    def setRouteDistance(self,name,distance="2"):
        """

        :param name:
        :param distance:
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=default-route-distance='+distance])
        return iface

    def setIpv6Interface(self,name,interface="none"):
        """

        :param name:
        :param interface: none, or other
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=ipv6-interface='+interface])
        return iface

    def setAuthentication(self,name,auth="none"):
        """

        :param name:
        :param auth: none,chap,pap
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=authentication='+auth])
        return iface

    def setUser(self,name,username):
        """

        :param name:
        :param username:
        :return:
        """
        if self.setAuthentication(name,"chap") or self.setAuthentication(name,"pap"):
            iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=user='+username])
        else:
            print("Error")
        return iface

    def setPassword(self,name,password):
        """

        :param name:
        :param password:
        :return:
        """
        if self.setAuthentication(name,"chap") or self.setAuthentication(name,"pap"):
            iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=password='+password])
        else:
            print("Error")
        return iface

    def setPassthroughInterface(self,name,interface="none"):
        """

        :param name:
        :param interface:none or physical iface
        :return:
        """
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=passthrough-interface='+interface])
        return iface

    def setPassthroughMac(self,name,interface,mac):
        """

        :param name:
        :param interface:
        :param mac:
        :return:
        """
        self.setPassthroughInterface(name,interface)
        iface = self.client.talk(['/interface/lte/apn/set', '=numbers=' + name, '=passthrough-mac='+mac])
        return iface