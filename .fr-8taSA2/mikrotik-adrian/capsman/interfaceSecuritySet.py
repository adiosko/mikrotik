from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceSecuritySet:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setSecurutyProfile(self,name,profile):
        """

        :param name:
        :param profile: profile created in security
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/set','=numbers='+name,'=security='+profile])
        return wifi

    def useSecurity(self,name,secName):
        """
        Method wil lset security profile earlier created in security
        :param name:
        :param secName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/interface/set','=numbers='+name,'=security='+secName])
        return wifi

    def setAuthenticationType(self,name,auth):
        """

        :param number:
        :param auth:  wpa-eap,wpa-psk,wpa2-eap,wpa2-psk
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.authentication-types=' + auth] )
        return wifi

    def setEncryption(self,name,encrypt="aes-com"):
        """

        :param name:
        :param encrypt: aes-com,tkip
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.encryption=' + encrypt] )
        return wifi

    def setGroupEncryption(self,name,ebcrypt="aes-com"):
        """

        :param name:
        :param ebcrypt:  aes-com,tkip
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.group-encryption=' + ebcrypt] )
        return wifi

    def setGroupKeyUpdate(self,name,update="00:00:00"):
        """

        :param name:
        :param update:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.group-key-update=' + update] )
        return wifi

    def setPassphrase(self,name,passphrase):
        """

        :param name:
        :param passphrase:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.passphrase=' + passphrase] )
        return wifi

    def setEapMethods(self,name,methods="eap-tls"):
        """

        :param name:
        :param methods: eap-tls,passthrough
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.eap-methods=' + methods] )
        return wifi

    def setEaoRadiusAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.eap-radius-accounting=yes'] )
        return wifi

    def unsetEapRadiusAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.eap-radius-accounting=no'] )
        return wifi

    def setTlsMode(self,name,mode="verify-certificate"):
        """

        :param name:
        :param mode: verify-certificate,dont-verify-certificate,no-certificates
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.tls-mode='+mode] )
        return wifi

    def setTlsCertificate(self,name,cert):
        """

        :param name:
        :param cert:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/interface/set', '=numbers=' + name, '=security.tls-certificate='+cert] )
        return wifi