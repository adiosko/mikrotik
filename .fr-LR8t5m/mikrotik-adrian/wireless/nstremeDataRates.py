from tikapy import TikapyClient
from tikapy import TikapySslClient

class NstreamSetDataRates:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setRatesB(self,name,rates="1Mbps,2Mbps,5.5Mbps,11Mbps"):
        """

        :param name:
        :param rates: 1Mbps,2Mbps,5.5Mbps,11Mbps
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/nsterme-dual/set','=numbers='+name,'=rates-b='+rates])
        return wifi

    def setRatesBG(self,name,rates="6Mbps,9Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps"):
        """

        :param name:
        :param rates:  6Mbps,9Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nsterme-dual/set', '=numbers=' + name, '=rates-a/g=' + rates] )
        return wifi