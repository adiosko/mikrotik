from tikapy import TikapyClient
from tikapy import TikapySslClient


class configWireless:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/configuration/set','=numbers='+name,'=name='+newName])
        return wifi

    def setMode(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=mode=ap'] )
        return wifi

    def setSsid(self,name,ssid):
        """

        :param name:
        :param ssid:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=ssid=' + ssid] )
        return wifi

    def hideSsid(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=hide-ssid=yes'] )
        return wifi

    def notHideSsid(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=hide-ssid=no'] )
        return wifi

    def setLoadBalacingGroup(self,name,group):
        """

        :param name:
        :param group:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=load-balancing-group='+group] )
        return wifi

    def setDistance(self,name,distance="indoors"):
        """

        :param name:
        :param distance: indoors,dynamic
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=distance='+distance] )
        return wifi

    def setHwRetries(self,name,retries="0"):
        """

        :param name:
        :param retries:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=hw-retries='+retries] )
        return wifi

    def setHwProtectionMOde(self,name,mode="none"):
        """

        :param name:
        :param mode: none,cts-to-self,rts-cts
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=hw-protection-mode='+mode] )
        return wifi

    def setFrameLifetime(self,name,lifetime="0.00"):
        """

        :param name:
        :param lifetime:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=frame-lifetime='+lifetime] )
        return wifi

    def setDisconnectionTimeout(self,name,timeout="00:00:00"):
        """

        :param name:
        :param timeout:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=disconnect-timeout=' + timeout] )
        return wifi

    def setKeepAliveFrame(self,name,mode="enabled"):
        """

        :param name:
        :param mode: enabled,disabled
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=keepalive-frames=' + mode] )
        return wifi

    def setCountry(self,name,country):
        """

        :param name:no-country-set or country
        :param country:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=country=' + country] )
        return wifi

    def setMaxStationCOunt(self,name,count="1"):
        """

        :param name:
        :param count:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=max-sta-count=' + count] )
        return wifi

    def setMultitaskHelper(self,name,helper="default"):
        """

        :param name:
        :param helper:default,disabled,full
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=multicast-helper=' + helper] )
        return wifi

    def setHtxChain(self,name,chain="0,1,2"):
        """

        :param name:
        :param chain:0,1,2
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=tx-chains=' + chain] )
        return wifi

    def setHRxChains(self,name,chains="0,1,2"):
        """

        :param name:
        :param chains:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=rx-chains=' + chains] )
        return wifi

    def setHtGuardInterval(self,name,interval="any"):
        """

        :param name:
        :param interval: any,long
        :return:
        """
        wifi = self.client.talk( ['/caps-man/configuration/set', '=numbers=' + name, '=guard-interval=' + interval] )
        return wifi