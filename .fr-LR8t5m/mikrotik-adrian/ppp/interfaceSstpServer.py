from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceSstpServer:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def enableServer(self):
        """
        Method will enable sstp server
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set','=enabled=yes'])
        return ppp

    def disableServer(self):
        """
        Method will disable server
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=enabled=no'])
        return ppp

    def setPort(self,port="443"):
        """
        Method will set port
        :param port:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=port='+port])
        return ppp

    def setMaxMtu(self,mtu="1500"):
        """
        Method will set max mtu
        :param mtu:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=max-mtu='+mtu])
        return ppp

    def setMaxMru(self,mru="1500"):
        """
        Method will set max mru
        :param mru:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=max-mru=' + mru])
        return ppp

    def setMrru(self,mrru="1500"):
        """
        Method will set mrru
        :param mrru:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=mrru=' + mrru])
        return ppp

    def setKeepaliveTimeout(self,timeout="60"):
        """
        Method will set keeplaive timeout
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=keepalive-timeout=' + timeout])
        return ppp

    def setDefaultProfile(self,profile="default"):
        """
        Method will set profile
        :param profile: default,default-encryption or custom
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=default-profile=' + profile])
        return ppp

    def setAuthentication(self,auth="mschap2"):
        """
        Method will set authentication
        :param auth: mschap1,mschap2,chap,pap
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=authentication=' + auth])
        return ppp

    def setCertificate(self,cert="none"):
        """
        Method will set cert
        :param cert: filename of cert
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=certificate='+cert])
        return ppp

    def setTlsVersion(self,tls="any"):
        """
        Method will set tls
        :param tls:any,only-1.2
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=rls-version='+tls])
        return ppp

    def verifyClientCertificate(self):
        """
        Method will verify client
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=verify-client-certificate=yes'])
        return ppp

    def notVerifyCLientCertificate(self):
        """
        Method will not verify client cert
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=verify-client-certificate=no'])
        return ppp

    def forceAes(self):
        """
        Method will force aes
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=force-aes=yes'])
        return ppp

    def unforceAes(self):
        """
        Method will unforce aes
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=force-aes=no'])
        return ppp

    def setPfs(self):
        """
        Method will enable pfs
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=pfs=yes'])
        return ppp

    def unsetPfs(self):
        """
        Method will enable pfs
        :return:
        """
        ppp = self.client.talk(['/interface/sstp-server/server/set', '=pfs=no'])
        return ppp