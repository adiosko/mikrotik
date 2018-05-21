from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppoeClientSetDialOut:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setService(self,name,service):
        """
        Method will set service
        :param name:
        :param service:
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/set','=numbers='+name,'=service-name='+service])
        return pppoe

    def setAcName(self,name,ac):
        """
        Method will set service
        :param name:
        :param ac:
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/set','=numbers='+name,'=ac-name='+ac])
        return pppoe

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/set','=numbers='+name,'=user='+user])
        return pppoe

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=password=' + password] )
        return pppoe

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encryption
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=profile=' + profile] )
        return pppoe

    def setKeepAliveTimeout(self,name,timeout="60"):
        """
        Method will set keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return pppoe

    def enableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=dial-on-demand=yes'] )
        return pppoe

    def disableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=dial-on-demand=no'] )
        return pppoe

    def enableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=add-default-route=yes'] )
        return pppoe

    def disableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=add-default-route=no'] )
        return pppoe

    def setDefRouteDistance(self,name,distance="1"):
        """
        Method will set def route distance
        :param name:
        :param distance:
        :return:
        """
        self.enableAddDefaultRoute(name)
        pppoe = self.client.talk( ['/interface/pppoe-client/set', '=numbers=' + name, '=default-route-distance=' + distance] )
        return pppoe

    def setAllow(self,name,auth="mschap2,mschap1,chap,pap"):
        """
        Method will rename iface
        :param name:
        :param auth: mschap2,mschap1,pap,chap
        :return:
        """
        pppoe = self.client.talk(['/interface/pppoe-client/set','=numbers='+name,'=allow='+auth])
        return pppoe