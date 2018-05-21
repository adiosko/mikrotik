from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceCap:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def enableCap(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/cap/set','=enabled=yes'])
        return wifi

    def disableCap(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=enabled=no'] )
        return wifi

    def setInterfaces(self,interface):
        """

        :param interface:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=interfaces='+interface] )
        return wifi

    def setCertificate(self,cert="none"):
        """

        :param cert:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=certificate='+cert] )
        return wifi

    def setDiscoveryInterfaces(self,interfaces):
        """

        :param interfaces:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=discovery-interfaces=yes'] )
        return wifi

    def lockToCapsman(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=lock-to-caps-man=yes'] )
        return wifi

    def unlockToCapsman(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=lock-to-caps-man=no'] )
        return wifi

    def setCapsManAddresses(self,addresses):
        """

        :param addresses:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=caps-man-addresses='+addresses] )
        return wifi

    def setCapsManNames(self,names):
        """

        :param names:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=caps-man-names='+names] )
        return wifi

    def setCapsmanCertficateComonNames(self,comonNames):
        """

        :param comonNames:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=caps-man-certificate-common-names='+comonNames] )
        return wifi

    def setBridge(self,bridge="none"):
        """

        :param bridge:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=bridge='+bridge] )
        return wifi

    def setStaticVirtual(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=static-virtual=yes'] )
        return wifi

    def unsetStaticVirtual(self):
        """

        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/cap/set', '=static-virtual=no'] )
        return wifi