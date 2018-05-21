from tikapy import TikapyClient
from tikapy import TikapySslClient

class NTPserver:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listServers(self):
        """
        Method will list all available ntp servers setup
        :return: list
        """
        server = self.client.talk(['/system/ntp/server/print'])
        if server == {}:
            print("No server found")
        else:
            print(server)
        return server

    def enableNtpServer(self):
        """
        Method will setup unicast server
        :return:list
        """
        server = self.client.talk(['/system/ntp/server/set','=enabled=yes'])
        return server

    def disableNtpServer(self):
        """
        Method will disable NTP server
        :return: list
        """
        server = self.client.talk( ['/system/ntp/server/set', '=enabled=no'] )
        return server


    def setBroadcastServer(self):
        """
        Method will enable bcast server
        :param address:  bcast address of server
        :return: list
        """
        server = self.client.talk(['/system/ntp/server/set','=enabled=yes','=broadcast=yes'])
        return server

    def setManyCastServer(self):
        """
        Method will setup manycast server
        :return: list
        """
        server = self.client.talk(['/system/ntp/server/set','=enabled=yes','=manycast=yes'])
        return server

    def setMUlticastServer(self):
        """
        Method will setup multicast server
        :return: list
        """
        server = self.client.talk(['/system/ntp/server/set','=enabled=yes','=multicast=yes'])
        return server

    def disableBroadcastServer(self):
        """
        Method will disable bcast server
        :return: list
        """
        server = self.client.talk( ['/system/ntp/server/set', '=enabled=yes', '=broadcast=no'] )
        return server

    def disableManycastServer(self):
        """
        Method will disable manycast server
        :return: list
        """
        server = self.client.talk( ['/system/ntp/server/set', '=enabled=yes', '=manycast=no'] )
        return server

    def disableMulticastServer(self):
        """
        Method will disable multicast nt server
        :return: list
        """
        server = self.client.talk( ['/system/ntp/server/set', '=enabled=yes', '=multicast=no'] )
        return server

    def setBroadcastAddresses(self,addresses):
        """
        Method will setup broadcast addresses
        :param addresses: bcast address
        :return: list
        """
        server = self.client.talk(['/system/ntp/server/set','=broadcast-addresses='+addresses])
        return server


