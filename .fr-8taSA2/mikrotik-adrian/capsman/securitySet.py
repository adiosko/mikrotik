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

    def setGroupEncryption(self,name,ebcrypt="aes-com"):
        """

        :param name:
        :param ebcrypt:  aes-com,tkip
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=group-encryption=' + ebcrypt] )
        return wifi

    def setGroupKeyUpdate(self,name,update="00:00:00"):
        """

        :param name:
        :param update:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=group-key-update=' + update] )
        return wifi

    def setPassphrase(self,name,passphrase):
        """

        :param name:
        :param passphrase:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=passphrase=' + passphrase] )
        return wifi

    def setEapMethods(self,name,methods="eap-tls"):
        """

        :param name:
        :param methods: eap-tls,passthrough
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=eap-methods=' + methods] )
        return wifi

    def setEaoRadiusAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=eap-radius-accounting=yes'] )
        return wifi

    def unsetEapRadiusAccounting(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=eap-radius-accounting=no'] )
        return wifi

    def setTlsMode(self,name,mode="verify-certificate"):
        """

        :param name:
        :param mode: verify-certificate,dont-verify-certificate,no-certificates
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=tls-mode='+mode] )
        return wifi

    def setTlsCertificate(self,name,cert):
        """

        :param name:
        :param cert:
        :return:
        """
        wifi = self.client.talk( ['/caps-man/security/set', '=numbers=' + name, '=tls-certificate='+cert] )
        return wifi