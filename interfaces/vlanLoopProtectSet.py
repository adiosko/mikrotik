from tikapy import TikapyClient
from tikapy import TikapySslClient


class vlanLoopProtectSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setMode(self,name,mode="default"):
        """

        :param name:
        :param mode: default,on,off
        :return:
        """
        vlan = self.client.talk(['/interface/vlan/set','=numbers='+name,'=loop-protect='+mode])
        return vlan

    def setSendInterval(self,name,interval="00:00:05"):
        """

        :param name:
        :param interval:
        :return:
        """
        vlan = self.client.talk(['/interface/vlan/set','=numbers='+name,'=loop-protect-send-interval='+interval])
        return vlan

    def setDisableTimeout(self,name,timeout="00:05:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        vlan = self.client.talk(['/interface/vlan/set','=numbers='+name,'=loop-protect-disable-time='+timeout])
        return vlan