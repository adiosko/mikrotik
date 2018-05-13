from tikapy import TikapyClient
from tikapy import TikapySslClient

class configRates:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)
        
    def setRates(self,name,ratesName):
        """
        
        :param name: 
        :param ratesName: 
        :return: 
        """
        wifi = self.client.talk(['/caps-man/configuration/set','=numbers='+name,'=rates='+ratesName])
        return wifi
    
    def setBasicRate(self,name,rate):
        """

        :param name:
        :param rate: 1Mbps,2Mbps,5.5Mbps,6Mbps,11Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps
        :return:
        """
        wifi = self.client.talk(['/caps-man/configuration/set','=numbers='+name,'=rates.basic='+rate])
        return wifi

    def setSuppoertRate(self,name,rate):
        """

        :param name:
        :param rate: 1Mbps,2Mbps,5.5Mbps,6Mbps,11Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rates.supported=' + rate] )
        return wifi

    def setHtBasic(self,name,ht):
        """

        :param name:
        :param ht:0-23
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rates.ht-basic-mcs=' + ht] )
        return wifi

    def setHtSupported(self,name,ht):
        """

        :param name:
        :param ht: 0-23
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rates.ht-supported-mcs=' + ht] )
        return wifi

    def setVhtBasic(self,name,vht="none"):
        """

        :param name:
        :param vht: none,mcs0-7,mcs0-8,mcs0-9
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rates.vht-basic-mcs=' + vht] )
        return wifi

    def setVhtSupport(self,name,vht="none"):
        """

        :param name:
        :param vht: none,mcs0-7,mcs0-8,mcs0-9
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rates.vht-supported-mcs=' + vht] )
        return wifi