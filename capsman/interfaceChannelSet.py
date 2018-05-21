from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceRatesSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def setChannelProfile(self, name, profile):
        """

        :param name: 
        :param profile: 
        :return: 
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel=' + profile] )
        return wifi
    
    def setFrequency(self,name,freq):
        """

        :param name:
        :param freq:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.frequency=' + freq] )
        return wifi

    def setControlCHannel(self,name,channel="5mhz"):
        """

        :param name:
        :param channel: 5mhz,10mhz,20mhz,40mhz-turbo
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.control-channel-width=' + channel] )
        return wifi

    def setExtensionCHannel(self,name,channel="disabled"):
        """

        :param name:
        :param channel:  Ce,Ceeeeeee,XXXX,disabled,eCee,eeCe,eeeC,eeeeCeee,eeeeeeCe,Ceee,XX,XXXXXXXX,eC,eCeeeeee,eeeCeeee
        eeeeeCee,eeeeeeeC
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.extension-channel=' + channel] )
        return wifi

    def setTxPower(self,name,power="0"):
        """

        :param name:
        :param power:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.tx-power=' + power] )
        return wifi

    def saveSelection(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.save-selected=yes'] )
        return wifi

    def notSaveSelected(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.save-selected=no'] )
        return wifi

    def setReselectInterval(self,name,interval="00:00:00"):
        """

        :param name:
        :param interval:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.reselect-interval='+interval] )
        return wifi

    def skipDfs(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.skip-dfs-channels=yes'] )
        return wifi

    def notSkipDfsChannels(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=channel.skip-dfs-channels=no'] )
        return wifi