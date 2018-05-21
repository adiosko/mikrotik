from tikapy import TikapyClient
from tikapy import TikapySslClient

class FloodPing:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setDefaultFloodPing(self,address):
        """
        Method will set defaulot flood ping with packet count 1000, pakcet size 1500 B, and timeout 1000
        :param address: address to server where to send big amount of data
        :return: list
        """
        ping = self.client.talk(['/tool/flood-ping','=address='+address])
        return ping

    def setCustomFields(self,address,packetcount=None,packetSize=None,Timeout = None):
        """
        Method will setup custom parameters
        :param address: address to send ping of death
        :param packetcount: packet counts   (optional) default 1000
        :param packetSize: pakcetsize def 1500 setup by MTU
        :param Timeout: timeout default 1000ms
        :return: list
        """
        if packetcount == None or packetSize == None or Timeout == None:
            ping = self.setDefaultFloodPing(address)
        else:
            ping = self.client.talk(['/tool/flood-ping','=address='+address,'=count='+packetcount,'=size='+packetSize,
                                     '=timeout='+Timeout])
        return  ping

