from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceL2tpServer:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def enableServer(self):
        """
        Method will enable l2tp server
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set','=enabled=yes'])
        return ppp

    def disableServer(self):
        """
        Method will disable server
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=enabled=no'])
        return ppp

    def setMaxsession(self,session):
        """
        Method will set port
        :param session:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=max-sessions='+session])
        return ppp

    def setMaxMtu(self,mtu="1450"):
        """
        Method will set max mtu
        :param mtu:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=max-mtu='+mtu])
        return ppp

    def setMaxMru(self,mru="1450"):
        """
        Method will set max mru
        :param mru:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=max-mru=' + mru])
        return ppp

    def setMrru(self,mrru="1500"):
        """
        Method will set mrru
        :param mrru:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=mrru=' + mrru])
        return ppp

    def setKeepaliveTimeout(self,timeout="60"):
        """
        Method will set keeplaive timeout
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=keepalive-timeout=' + timeout])
        return ppp

    def setDefaultProfile(self,profile="default"):
        """
        Method will set profile
        :param profile: default,default-encryption or custom
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=default-profile=' + profile])
        return ppp

    def setAuthentication(self,auth="mschap2"):
        """
        Method will set authentication
        :param auth: mschap1,mschap2,chap,pap
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=authentication=' + auth])
        return ppp

    def notUseIpsec(self):
        """
        Method will disable ipsec for l2tp
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=use-ipsec=no'])
        return ppp

    def useIpsec(self,usage="yes"):
        """
        Method will set ipsec usagfe
        :param usage: yes,required
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=use-ipsec=' + usage])
        return ppp

    def setIpsecSecret(self,secret):
        """
        Method will set ipsec secret
        :param secret:
        :return:
        """
        self.useIpsec()
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=ipsec-secret=' + secret])
        return ppp

    def setCallerIdType(self,caller="ip-address"):
        """
        Method wil lset caller id
        :param caller: ip-address,number
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=caller-id-type=' + caller])
        return ppp

    def enableOneSessionPerHost(self):
        """
        Method will enable one session per host
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=one-session-per-host=yes'])
        return ppp

    def disableOneSessionPerHost(self):
        """
        Method will enable one session per host
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=one-session-per-host=no'])
        return ppp

    def allowFastPath(self):
        """
        Method will allow fast  path
        :return:
        """

    def enableFastPAth(self):
        """
        Method will enable one session per host
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=allow-fast-path=yes'])
        return ppp

    def disableFastPAth(self):
        """
        Method will enable one session per host
        :return:
        """
        ppp = self.client.talk(['/interface/l2tp-server/server/set', '=allow-fast-path=no'])
        return ppp