from tikapy import TikapyClient
from tikapy import TikapySslClient

class pppoeSettings:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setName(self,name,newName):
        """
        Method will rename service
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name,'=service-name='+newName])
        return ppp

    def setInterface(self,name,iface):
        """
        Method will set interface
        :param name:
        :param iface:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=interface=' + iface])
        return ppp

    def setMaxMtu(self,name,mtu="512"):
        """
        Method will set max mtu
        :param name:
        :param mtu:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=max-mtu=' + mtu])
        return ppp

    def setMaxMru(self,name,mru="512"):
        """
        Method will set max mru
        :param name:
        :param mru:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=max-mru=' + mru])
        return ppp

    def setMrru(self,name,mrru="1500"):
        """
        Method will set max mrru
        :param name:
        :param mrru:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=mrru=' + mrru])
        return ppp

    def setKeepAliveTimeout(self,name,timeout="10"):
        """
        Method will set max keepalive timeout in secs
        :param name:
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=keepalive-timeout=' + timeout])
        return ppp

    def setDefaultProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encruption or custom
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=default-profile=' + profile])
        return ppp

    def enableOneSessionPerHost(self,name):
        """
        Method will enable one session per host
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=one-session-per-host=yes'])
        return ppp

    def disableOneSessionPerHost(self,name):
        """
        Method will enable one session per host
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=one-session-per-host=no'])
        return ppp

    def setMaxSessions(self,name,maxsession):
        """
        Method will set max session limit
        :param name:
        :param maxsession:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=max-sessions='+maxsession])
        return ppp

    def setPadoDelay(self,name,pado="0"):
        """
        Method will set pado delay
        :param name:
        :param pado: in ms
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=pado-delay='+pado])
        return ppp

    def enableMschap2(self,name):
        """
        Method will enable mschap
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=authentication=mschap2'])
        return ppp


    def enableMschap1(self,name):
        """
        Method will enable mschap
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=authentication=mschap1'])
        return ppp

    def enablePap(self,name):
        """
        Method will enable pap
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=authentication=pap'])
        return ppp

    def enableChap(self,name):
        """
        Method will enable chap
        :param name:
        :return:
        """
        ppp = self.client.talk(['/interface/pppoe-server/server/set', '=numbers=' + name, '=authentication=chap'])
        return ppp