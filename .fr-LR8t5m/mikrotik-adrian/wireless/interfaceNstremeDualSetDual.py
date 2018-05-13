from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceNstreamDualSetDual:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setTxRadio(self,name,txradio):
        """
        Method will set name
        :param name:
        :param txradio:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/nstreme-dual/set','=numbers='+name,'=tx-radio='+txradio])
        return wifi

    def setRxRadio(self,name,radio):
        """

        :param name:
        :param radio:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=rx-radio=' + radio] )
        return wifi

    def setRemoteMac(self,name,mac="00:00:00:00:00:00"):
        """

        :param name:
        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=remote-mac=' + mac] )
        return wifi

    def setTxBand(self,name,band):
        """

        :param name:
        :param band:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=tx-band=' + band] )
        return wifi

    def setTxChannelWidth(self,name,width):
        """

        :param name:
        :param width:  5mhz,10mhz,20mhz,40mhz
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=tx-channel-width=' + width] )
        return wifi

    def setTxFrequency(self,name,frequency="5180"):
        """

        :param name:
        :param frequency:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=tx-frequency=' + frequency] )
        return wifi

    def setRxBand(self, name, band):
        """

        :param name:
        :param band:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=rx-band=' + band] )
        return wifi

    def setRxChannelWidth(self, name, width):
        """

        :param name:
        :param width:  5mhz,10mhz,20mhz,40mhz
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=rx-channel-width=' + width] )
        return wifi

    def setRxFrequency(self, name, frequency="5320"):
        """

        :param name:
        :param frequency:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=rx-frequency=' + frequency] )
        return wifi

    def enableCsma(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=disable-csma=no'] )
        return wifi

    def disableCsma(self, name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=disable-csma=yes'] )
        return wifi

    def setFramerPolicy(self,name,size="none"):
        """

        :param name:
        :param size: none,best-fit,exact-size
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=framer-policy='+size] )
        return wifi

    def setFrameLimit(self,name,limit="2560"):
        """

        :param name:
        :param limit:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/nstreme-dual/set', '=numbers=' + name, '=framer-limit='+limit] )
        return wifi