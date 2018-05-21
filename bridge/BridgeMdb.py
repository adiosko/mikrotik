from tikapy import TikapyClient
from tikapy import TikapySslClient

class BridgeMdb:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMdb(self):
        """
        Method will list mdb
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/mdb/print'])
        for i in bridge:
            print(bridge[i])
        return bridge

    def setPort(self,number,port):
        """
        Method will set port
        :param number:
        :return:
        """
        bridge = self.client.talk(['/interface/bridge/mdb/set','=numbers='+number,'=ports='+port])
        return bridge