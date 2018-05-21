from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimSettings:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def enableSwitchToSpt(self):
        """
        Method will switch to spt
        :return:
        """
        pim = self.client.talk(['/routing/pim/set','=switch-to-spt=yes'])
        return pim

    def disableSwitchToSpm(self):
        """
        Method will disable spm
        :return:
        """
        pim = self.client.talk( ['/routing/pim/set', '=switch-to-spt=no'] )
        return pim

    def setSptInterval(self,interval="00:01:40"):
        """
        Method will set spt interval
        :return:
        """
        pim = self.client.talk( ['/routing/pim/set', '=switch-to-spt-interval='+interval] )
        return pim

    def setSptByte(self,bytes="0"):
        """
        Method will set spm bytes
        :param bytes:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/set', '=switch-to-spt-bytes='+bytes] )
        return pim