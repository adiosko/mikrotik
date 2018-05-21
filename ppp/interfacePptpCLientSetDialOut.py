from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePptpClientSetDialOut:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setConnectTo(self,name,conect):
        """

        :param name:
        :param conect:
        :return:
        """
        pptp = self.client.talk(['/interface/pptp-client/set','=numbers='+name,'=connect-to'+conect])
        return pptp

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        pptp = self.client.talk(['/interface/pptp-client/set','=numbers='+name,'=user='+user])
        return pptp

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=password=' + password] )
        return pptp

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encryption
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=profile=' + profile] )
        return pptp

    def setKeepAliveTimeout(self,name,timeout="30"):
        """
        Method will set keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return pptp

    def enableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=dial-on-demand=yes'] )
        return pptp

    def disableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=dial-on-demand=no'] )
        return pptp

    def enableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=add-default-route=yes'] )
        return pptp

    def disableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=add-default-route=no'] )
        return pptp

    def setDefRouteDistance(self,name,distance="1"):
        """
        Method will set def route distance
        :param name:
        :param distance:
        :return:
        """
        self.enableAddDefaultRoute(name)
        pptp = self.client.talk( ['/interface/pptp-client/set', '=numbers=' + name, '=default-route-distance=' + distance] )
        return pptp

    def setAllow(self,name,auth="mschap2,mschap1,chap,pap"):
        """
        Method will rename iface
        :param name:
        :param auth: mschap2,mschap1,pap,chap
        :return:
        """
        pptp = self.client.talk(['/interface/pptp-client/set','=numbers='+name,'=allow='+auth])
        return pptp