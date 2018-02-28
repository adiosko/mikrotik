from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWirelessSmiffer:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableMultipleChannels(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/sniffer/set','=multiple-channels=yes'])
        return wifi

    def disableMultipleChannels(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/sniffer/set','=multiple-channels=no'])
        return wifi

    def enableOnlyHeaders(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=only-headers=yes'] )
        return wifi

    def disableOnlyHeaders(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=only-headers=no'] )
        return wifi

    def enableReceiveErrors(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=receive-errors=yes'] )
        return wifi

    def disableReceiveErrors(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=receive-errors=no'] )
        return wifi

    def setChannelTime(self,time="00:00:20"):
        """

        :param time: in secs
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=channel-time='+time] )
        return wifi

    def setMemoryLimit(self,limit="10"):
        """

        :param limit: in KiB
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=memory-limit=' + limit] )
        return wifi

    def setFileName(self,fileName):
        """

        :param fileName:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=file-name=' + fileName] )
        return wifi

    def setFileLimit(self,limit="10"):
        """

        :param limit: KiB
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=file-limit=' + limit] )
        return wifi

    def enableStreaming(self):
        """
        Method will enable sreaming
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=streaming-enabled=yes'] )
        return wifi

    def disableStreaming(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=streaming-enabled=no'] )
        return wifi

    def setStreamingServer(self,server="0.0.0.0"):
        """

        :param server:
        :return:
        """
        self.enableStreaming()
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=streaming-server='+server] )
        return wifi

    def setStreamingMaxRate(self,pps):
        """

        :param pps: pakcet per second
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/sniffer/set', '=streaming-max-rate='+pps] )
        return wifi