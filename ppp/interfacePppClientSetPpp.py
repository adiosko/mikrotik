from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppClientSetPpp:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/set','=numbers='+name,'=user='+user])
        return ppp

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=password=' + password] )
        return ppp

    def setRemoteAddress(self,name,addr):
        """
        Method will set remote address
        :param name:
        :param addr:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=remote-address=' + addr] )
        return ppp

    def setKeepAliveTimeout(self,name,timeout="30"):
        """
        Method will set keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return ppp

    def enableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=dial-on-demand=yes'] )
        return ppp

    def disableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=dial-on-demand=no'] )
        return ppp

    def enableUsePeerDns(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=use-peer-dns=yes'] )
        return ppp

    def disableUsePeerDns(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=use-peer-dns=no'] )
        return ppp

    def enableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=add-default-route=yes'] )
        return ppp

    def disableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=add-default-route=no'] )
        return ppp

    def setDefRouteDistance(self,name,distance="1"):
        """
        Method will set def route distance
        :param name:
        :param distance:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=default-route-distance=' + distance] )
        return ppp