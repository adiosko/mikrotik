from tikapy import TikapyClient
from tikapy import TikapySslClient

class HotspotWalledGarden:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listWalled(self):
        """
        Method will list walled garden rules
        :return:
        """
        hotspot = self.client.talk(['/ip/hotspot/walled-garden/print'])
        for i in hotspot:
            print(hotspot[i]['action']+"\t"+hotspot[i]['dst-port'])
        return hotspot

    def addWalled(self,action="allow"):
        """
        Method will add garden
        :param action: allow,deny
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/add','=action='+action] )
        return hotspot

    def removeGarden(self,number):
        """
        Method will remove garden
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/remove', '=numbers=' + number] )
        return hotspot

    def enableGarden(self,number):
        """

        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/enable', '=numbers=' + number] )
        return hotspot

    def disableGarden(self,number):
        """
        Methgod will disable garden
        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/disable', '=numbers=' + number] )
        return hotspot

    def commentGarden(self,number,comment):
        """

        :param number:
        :param comment:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/comment', '=numbers=' + number,'=comment='+comment] )
        return hotspot

    def resetCounters(self,number):
        """

        :param number:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/reset-counters', '=numbers=' + number] )
        return hotspot

    def resetAllCounters(self):
        """

        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/reset-counters-all'] )
        return hotspot

    def setAction(self,number,action):
        """
        Method will list actions
        :param number:
        :param action: allow,deny
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=action=' + action] )
        return hotspot

    def setServer(self,number,server):
        """

        :param number:
        :param server: name of server, !
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=server=' + server] )
        return hotspot

    def setSrcAddress(self,number,src):
        """
        Method will set src address
        :param number:
        :param src:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=src-address=' + src] )
        return hotspot

    def setMethod(self,number,mtd):
        """
        Method will set dst
        :param number:
        :param mtd:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=method=' + mtd] )
        return hotspot

    def setDstHosts(self,number,host):
        """
        Method will set dst port
        :param number:
        :param host:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=dst-host=' + host] )
        return hotspot

    def setDstPort(self, number, port):
        """
        Method will set dst port
        :param number:
        :param host:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=dst-port=' + port] )
        return hotspot

    def setPath(self,number,path):
        """
        Method will set path
        :param number:
        :param path:
        :return:
        """
        hotspot = self.client.talk( ['/ip/hotspot/walled-garden/set', '=numbers=' + number, '=path=' + path] )
        return hotspot

