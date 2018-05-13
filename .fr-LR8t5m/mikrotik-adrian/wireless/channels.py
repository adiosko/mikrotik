from tikapy import TikapyClient
from tikapy import TikapySslClient

class Channels:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listChannels(self):
        """
        Method will list channels
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/print'])
        print("List\tName\tFrequency\twidth\tband")
        for i in wifi:
            print(wifi[i]['list']+"\t"+wifi[i]['name']+"\t"+wifi[i]['frequency']+"\t"+wifi[i]['width']+"\t"+wifi[i]['band'])
        return wifi

    def addChannel(self,listName,band,frequency,width):
        """
        Method will add channel
        :param listName: name of list
        :param band: 2ghz-b,2ghz-b/g,2ghz-b/g/n,2ghz-onlyg,2ghz-onlyn,5ghz-a,5ghz-a/n,5ghz-a/n/ac,5ghz-onlyac,5ghz-onlyn
        :param frequency: frequency f.e 2412 in Mhz
        :param width: 20MMhz
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/add','=list='+listName,'=frequency='+frequency,'=band='+band,'=width='+width])
        return wifi

    def removeChannel(self,number):
        """
        Method will remove channel
        :param number:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/remove','=numbers='+number])
        return wifi

    def enableChannel(self,number):
        """
        Method will remove channel
        :param number:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/enable','=numbers='+number])
        return wifi

    def disableChannel(self,number):
        """
        Method will remove channel
        :param number:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/disable','=numbers='+number])
        return wifi

    def commentChannel(self,number,comment):
        """
        Method will remove channel
        :param number:
        :param comment:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/channels/comment','=numbers='+number,'=comment='+comment])
        return wifi