from tikapy import TikapyClient
from tikapy import TikapySslClient

class ChannelsSet:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setList(self,number,listName):
        """
        Method will set listname
        :param number:
        :param listName:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/set','=numbers='+number,'=list='+listName])
        return wifi

    def setName(self,name,newName):
        """
        Method will rename
        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/channels/set', '=numbers=' + name, '=name=' + newName] )
        return wifi

    def setFrequency(self,number,freq="2412.000"):
        """
        Method will set frequency
        :param number:
        :param freq:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/channels/set', '=numbers=' + number, '=frequency=' + freq] )
        return wifi

    def setWidth(self,number,width):
        """
        Method will set width
        :param number:
        :param width: 20,40
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/channels/set', '=numbers=' + number, '=width=' + width] )
        return wifi

    def setBand(self,number,band="2ghz-b/g/n"):
        """
        Method will set band
        :param number:
        :param band: 2ghz-b,2ghz-b/g,2ghz-b/g/n,2ghz-onlyg,2ghz-onlyn,5ghz-a,5ghz-a/n,5ghz-a/n/ac,5ghz-onlyac,5ghz-onlyn
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/channels/set', '=numbers=' + number, '=band=' + band] )
        return wifi

    def setExtensionCahnnel(self,number,channel="Ce"):
        """
        Method will set extension channel
        :param number:
        :param channel: Ce,Ceee,disabled,eC,eCee,eeCe,eeeC
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/channels/set', '=numbers=' + number, '=extension-channel=' + channel] )
        return wifi