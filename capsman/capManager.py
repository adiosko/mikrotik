from tikapy import TikapyClient
from tikapy import TikapySslClient

class capManager:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def enableCap(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set','=enabled=yes'])
        return wifi

    def disableCap(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=enabled=no'])
        return wifi

    def setCertificate(self,cert):
        """

        :param cert:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=certificate='+cert])
        return wifi

    def setCaCertificate(self,cacert):
        """

        :param cacert:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=ca-cert='+cacert])
        return wifi

    def enableRequierePeerCertificate(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=require-peer-certificate=yes'])
        return wifi

    def disableRequierePeerCertificate(self):
        """

        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=require-peer-certificate=no'])
        return wifi

    def setPackagePath(self,path):
        """

        :param path:
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=package-path='+path])
        return wifi

    def setUpgradePolicy(self,policy="none"):
        """

        :param policy:  none,require-same-version,suggest-same-version
        :return:
        """
        wifi = self.client.talk(['/caps-man/manager/set', '=upgrade-policy='+policy])
        return wifi