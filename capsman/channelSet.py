from tikapy import TikapyClient
from tikapy import TikapySslClient

class channelsSet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/channel/set','=numbers='+name,'=name='+newName])
        return wifi

    def setFrequency(self,name,freq):
        """

        :param name:
        :param freq:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=frequency=' + freq] )
        return wifi

    def setControlCHannel(self,name,channel="5mhz"):
        """

        :param name:
        :param channel: 5mhz,10mhz,20mhz,40mhz-turbo
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=control-channel-width=' + channel] )
        return wifi

    def setExtensionCHannel(self,name,channel="disabled"):
        """

        :param name:
        :param channel:  Ce,Ceeeeeee,XXXX,disabled,eCee,eeCe,eeeC,eeeeCeee,eeeeeeCe,Ceee,XX,XXXXXXXX,eC,eCeeeeee,eeeCeeee
        eeeeeCee,eeeeeeeC
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=extension-channel=' + channel] )
        return wifi

    def setTxPower(self,name,power="0"):
        """

        :param name:
        :param power:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=tx-power=' + power] )
        return wifi

    def saveSelection(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=save-selected=yes'] )
        return wifi

    def notSaveSelected(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=save-selected=no'] )
        return wifi

    def setReselectInterval(self,name,interval="00:00:00"):
        """

        :param name:
        :param interval:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=reselect-interval='+interval] )
        return wifi

    def skipDfs(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=skip-dfs-channels=yes'] )
        return wifi

    def notSkipDfsChannels(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/channel/set', '=numbers=' + name, '=skip-dfs-channels=no'] )
        return wifi