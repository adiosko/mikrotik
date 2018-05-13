from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotIpBinding:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listBindings(self):
        """
        Method will list ip bindings
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/ip-binding/print'])
        if hotspot == {}:
            print("No binding found")
        else:
            print("MAC\tServer")
            for i in hotspot:
                print(hotspot[i]['mac-address']+"\t"+hotspot[i]['address']+"\t"+hotspot[i]['to-address']+"\t"+hotspot[i]['server'])
        return hotspot

    def addBinding(self,mac):
        """
        Method will add binding
        :param mac:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/add','=mac-address='+mac] )
        return hotspot

    def removeBinding(self,number):
        """
        Method will remove binding
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/remove','=numbers='+number] )
        return hotspot

    def enableBinding(self,number):
        """

        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/enable', '=numbers=' + number] )
        return hotspot

    def disableBinding(self,number):
        """
        Method will disable binding
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/disable', '=numbers=' + number] )
        return hotspot

    def commentBinding(self,number,comment):
        """
        Method will comment binding
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/comment', '=numbers=' + number,'=comment='+comment] )
        return hotspot

    def setMac(self,number,mac):
        """
        Method will set mac address
        :param number:
        :param mac:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/set', '=numbers=' + number,'=mac-address='+mac] )
        return hotspot

    def setAddress(self,number,address):
        """
        Method will set address
        :param name:
        :param address:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/set', '=numbers=' + number,'=address='+address] )
        return hotspot

    def setToAddress(self,number,address):
        """
        Method will set translation address
        :param number:
        :param address:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/set', '=numbers=' + number,'=to-address='+address] )
        return hotspot

    def setServer(self,number,server="all"):
        """
        Method will set server
        :param name:
        :param server:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/set', '=numbers=' + number, '=server=' + server] )
        return hotspot

    def setType(self,number,service="regular"):
        """
        Method will set type f service
        :param number:
        :param service:regular,blocked,bypass
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/ip-binding/set', '=numbers=' + number, '=type=' + service] )
        return hotspot
