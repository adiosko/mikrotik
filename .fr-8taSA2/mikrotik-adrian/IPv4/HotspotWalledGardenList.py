from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotWalledGardenList:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listWaledGardenList(self):
        """
        Method will list walled garden lists
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/walled-garden/ip/print'])
        print("Action\tServer\tSrc\tProtocol\tDst port")
        for i in hotspot:
            print(hotspot[i]['action']+"\t"+hotspot[i]['server']+"\t"+hotspot[i]['src-address']+"\t"+hotspot[i]['protocol']+"\t"+hotspot[i]['dst-port'])
        return hotspot

    def addWalled(self, action="allow"):
        """
        Method will add garden
        :param action: allow,deny
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/add', '=action=' + action] )
        return hotspot

    def removeGarden(self, number):
        """
        Method will remove garden
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/remove', '=numbers=' + number] )
        return hotspot

    def enableGarden(self, number):
        """

        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/enable', '=numbers=' + number] )
        return hotspot

    def disableGarden(self, number):
        """
        Methgod will disable garden
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/disable', '=numbers=' + number] )
        return hotspot

    def commentGarden(self, number, comment):
        """

        :param number:
        :param comment:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/comment', '=numbers=' + number, '=comment=' + comment] )
        return hotspot

    def setAction(self, number, action):
        """
        Method will list actions
        :param number:
        :param action: allow,deny,reject
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=action=' + action] )
        return hotspot

    def setServer(self, number, server):
        """

        :param number:
        :param server: name of server, !
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=server=' + server] )
        return hotspot

    def setSrcAddress(self, number, src):
        """
        Method will set src address
        :param number:
        :param src:!,src
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=src-address=' + src] )
        return hotspot

    def setDstAddress(self, number, dst):
        """
        Method will set src address
        :param number:
        :param src:!,src
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=dst-address=' + dst] )
        return hotspot

    def setProtocol(self, number, prot):
        """
        Method will set dst
        :param number:
        :param prot: !, protocol
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=protocol=' + prot] )
        return hotspot

    def setDstHosts(self, number, host):
        """
        Method will set dst port
        :param number:
        :param host:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=dst-host=' + host] )
        return hotspot

    def setDstPort(self, number, port):
        """
        Method will set dst port
        :param number:
        :param host:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/ip/set', '=numbers=' + number, '=dst-port=' + port] )
        return hotspot