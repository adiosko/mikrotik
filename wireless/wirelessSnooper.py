from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceWirelessSnooper:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def enableMultipleCHannels(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/snooper/set','=multiple-channels=yes'])
        return wifi

    def disableMultipleChannels(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/snooper/set', '=multiple-channels=no'] )
        return wifi

    def setCHannelTime(self,time="200"):
        """

        :param time:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/snooper/set', '=channel-time='+time] )
        return wifi

    def enableReceiveErrors(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/snooper/set', '=receive-errors=yes'] )
        return wifi

    def disableReceiveErrors(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/snooper/set', '=receive-errors=no'] )
        return wifi