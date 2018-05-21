from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotServer:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listServers(self):
        """
        Method will list servers
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/print'])
        if hotspot == {}:
            print("No hotspot found")
        else:
            print("Name\tInterface\tProfile")
            for i in hotspot:
                print(hotspot[i]['name']+"\t"+hotspot[i]['interface']+"\t"+hotspot[i]['profile'])
        return hotspot

    def addServer(self,name,interface):
        """
        Method will add hotspot server
        :param name:
        :param interface:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/add','=name='+name,'=interface='+interface] )
        return hotspot

    def removeServer(self,name):
        """
        Method will remove server
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/remove', '=numbers=' + name] )
        return hotspot

    def enableServer(self,name):
        """

        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/enable', '=numbers=' + name] )
        return hotspot

    def disbaleServer(self,name):
        """

        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/disable', '=numbers=' + name] )
        return hotspot

    def setName(self,name,newName):
        """
        Method will rename server
        :param name:
        :param newName:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name,'=name='+newName] )
        return hotspot

    def setInterface(self,name,interface):
        """
        Method will set interface
        :param name:
        :param interface:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=interface=' + interface] )
        return hotspot

    def setAddressPool(self,name,pool):
        """
        Method will set pool
        :param name:
        :param pool: pool created in pool
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=address-pool=' + pool] )
        return hotspot

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=profile=' + profile] )
        return hotspot

    def setIdleTimeout(self,name,timeout="00:00:00"):
        """
        Method will set idle timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=idle-timeout=' + timeout] )
        return hotspot

    def setKeepaliveTimeout(self,name,timeout="00:00:00"):
        """
        Method wil lset keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return hotspot

    def setLoginTimeout(self,name,timeout="00:00:00"):
        """
        Method will set login timeout
        :param name:
        :param timeout:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/set', '=numbers=' + name, '=login-timeout=' + timeout] )
        return hotspot

    def resetHtml(self,name):
        """
        Method will reset html
        :param name:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/reste-html', '=numbers=' + name] )
        return hotspot






