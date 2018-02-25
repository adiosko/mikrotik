from tikapy import TikapyClient
from tikapy import TikapySslClient
from wireless import securityProfileSetGeneral

class securityProfileSetEap:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)
        security = securityProfileSetGeneral.securityProfileSetGeneral(address,username,password)

    def setEapMethods(self,name,eap="passthrough"):
        """

        :param name:
        :param eap: eap-tls,eap-tls-mschapv2,passthrough,peap
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=eap-methods='+eap])
        return wifi

    def setTlsMode(self,name,tls="no-certificates"):
        """
        Method will set tls method
        :param name:
        :param tls: no-certificates,dont-verify-certificates,verify-certificate,verify-certificate-with-crl
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=tls-mode=' + tls] )
        return wifi

    def setTlsCertificate(self,name,cert="none"):
        """
        Method wil lset tls cert
        :param name:
        :param cert:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=tls-certificate=' + cert] )
        return wifi

    def enableMschapv2(self,name):
        """
        Method will enable mschapv2
        :param name:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=eap-methods=eao-mschapv2'] )
        return wifi

    def setMschapUsername(self,name,user):
        """

        :param name:
        :param user:
        :return:
        """
        self.enableMschapv2(name)
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=mschapv2-username=' + user] )
        return wifi

    def setMschapPassword(self,name,password):
        """

        :param name:
        :param password:
        :return:
        """
        self.enableMschapv2(name)
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=mschapv2-password=' + password] )
        return wifi