from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePptpServer:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def enableServer(self):
        """
        Method will enable pptp server
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set','=enabled=yes'])
        return ppp

    def disableServer(self):
        """
        Method will disable server
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=enabled=no'])
        return ppp

    def setMaxMtu(self,mtu="1460"):
        """
        Method will set max mtu
        :param mtu:
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=max-mtu='+mtu])
        return ppp

    def setMaxMru(self,mru="1460"):
        """
        Method will set max mru
        :param mru:
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=max-mru=' + mru])
        return ppp

    def setMrru(self,mrru="1500"):
        """
        Method will set mrru
        :param mrru:
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=mrru=' + mrru])
        return ppp

    def setKeepaliveTimeout(self,timeout="30"):
        """
        Method will set keeplaive timeout
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=keepalive-timeout=' + timeout])
        return ppp

    def setDefaultProfile(self,profile="default"):
        """
        Method will set profile
        :param profile: default,default-encryption or custom
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=default-profile=' + profile])
        return ppp

    def setAuthentication(self,auth="mschap2,mschap1"):
        """
        Method will set authentication
        :param auth: mschap1,mschap2,chap,pap
        :return:
        """
        ppp = self.client.talk(['/interface/pptp-server/server/set', '=authentication=' + auth])
        return ppp



