from tikapy import TikapyClient
from tikapy import TikapySslClient

class UpnpInterface:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listInterface(self):
        """
        Method will list upnp interfaces
        :return:
        """
        upnp = self.client.talk(['/ip/upnp/interfaces/print'])
        print("Interface\tType")
        for i in upnp:
            print(upnp[i]['interface']+"\t"+upnp[i]['type'])
        return upnp

    def addInterface(self,interface,ifaceType="internal"):
        """
        Method will add upnp inerface
        :param interface:
        :param ifaceType:internal, external
        :return:
        """
        upnp = self.client.talk(['/ip/upnp/interfaces/add','=interface='+interface,'=type='+ifaceType])
        return upnp

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        upnp = self.client.talk(['/ip/upnp/interfaces/remove','=numbers='+number])
        return upnp

    def enableInterface(self,number):
        """
        Method will enable interface
        :param number:
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/interfaces/enable', '=numbers=' + number] )
        return upnp

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/interfaces/disable', '=numbers=' + number] )
        return upnp

    def setInterface(self,number,iface):
        """
        Method will set interface
        :param number:
        :param iface:
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/interfaces/set', '=numbers=' + number,'=interface='+iface] )
        return upnp

    def setInterfaceTypeInteral(self,number):
        """
        Method will set interface
        :param number:
        :param iface:
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/interfaces/set', '=numbers=' + number, '=type=internal'] )
        return upnp

    def setInterfaceTypeExternal(self,number,IP):
        """
        Method will se texternal interface ip
        :param number:
        :param IP:
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/interfaces/set', '=numbers=' + number, '=type=external','=forced-ip=' + IP] )
        return upnp

    