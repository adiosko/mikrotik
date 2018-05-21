from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWirelessAlignement:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setFrameSize(self,frame="300"):
        """

        :param frame:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/align/set','=frame-size='+frame])
        return wifi

    def setActiveMode(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=active-mode=yes'] )
        return wifi

    def unsetActiveMode(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=active-mode=no'] )
        return wifi

    def receiveAll(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=receive-all=yes'] )
        return wifi

    def notreceiveAll(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=receive-all=no'] )
        return wifi

    def filterMacAddress(self,mac="00:00:00:00:00:00"):
        """

        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=filter-mac='+mac] )
        return wifi

    def ssidAll(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=ssid-all=yes'] )
        return wifi

    def unssidAll(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=ssid-all=no'] )
        return wifi

    def setFps(self,fps="25"):
        """

        :param fps:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=frame-per-second='+fps] )
        return wifi

    def setAudioMonitor(self,mac="00:00:00:00:00:00"):
        """

        :param mac:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=audio-monitor='+mac] )
        return wifi

    def setAudioMin(self,minimum="-100"):
        """

        :param minimum:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=audio-min=' + minimum] )
        return wifi

    def setAudioMax(self,maximum="-20"):
        """

        :param maximum:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/align/set', '=audio-max=' + maximum] )
        return wifi
