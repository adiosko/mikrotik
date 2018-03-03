from tikapy import TikapyClient
from tikapy import TikapySslClient

class securitySet:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/security/set','=numbers='+name,'=name='+newName])
        return wifi

    def setAuthenticationType(self,name,auth):
        """

        :param number:
        :param auth:  wpa-eap,wpa-psk,wpa2-eap,wpa2-psk
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=authentication-types=' + auth] )
        return wifi

    def setEncryption(self,name,encrypt="aes-com"):
        """

        :param name:
        :param encrypt: aes-com,tkip
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=encryption=' + encrypt] )
        return wifi

    """
    !!!!!! pokracovat dalej!!!!!!!
    """