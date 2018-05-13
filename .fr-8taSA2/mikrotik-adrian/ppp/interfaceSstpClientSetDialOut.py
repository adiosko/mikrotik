from tikapy import TikapyClient
from tikapy import TikapySslClient


class interfaceSstpClientSetDialOut:
    def __init__(self, address, username, password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def setConnectTo(self,name,conect):
        """

        :param name:
        :param conect:
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set','=numbers='+name,'=connect-to'+conect])
        return sstp

    def setPort(self,name,port):
        """

        :param name:
        :param conect:
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set','=numbers='+name,'=port='+port])
        return sstp

    def setProxy(self,name,proxy,port):
        """

        :param name:
        :param proxy:
        :param port:
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set','=numbers='+name,'=http-proxy='+proxy+":"+port])
        return sstp

    def setCertificate(self,name,cert):
        """

        :param name:
        :param cert:
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set', '=numbers=' + name, '=certificate=' + cert] )
        return sstp

    def setTls(self,name,tls="any"):
        """

        :param name:
        :param tls:any,only-1.2
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=tls-version=' + tls] )
        return sstp
    
    def enableVerifyclientCertificate(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=verify-client-certificate=yes'] )
        return sstp
    
    def disableVerifyclientCertificate(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=verify-client-certificate=no'] )
        return sstp
    
    def enableVerifyclientAddressFromCertificate(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, 
                                  '=verify-client-address-from-certificate=yes'] )
        return sstp
    
    def disableVerifyclientAddressFromCertificate(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, 
                                  '=verify-client-address-from-certificate=no'] )
        return sstp
    
    def enablePfs(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name,'=pfs=yes'] )
        return sstp
    
    
    def disablePfs(self,name):
        """
        Method will e\verify cert
        :param name: 
        :return: 
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name,'=pfs=no'] )
        return sstp
    
    def setUser(self,name,user):
        """
        Method will set user
        :param name:
        :param user:
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set','=numbers='+name,'=user='+user])
        return sstp
    
    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=password=' + password] )
        return sstp

    def setProfile(self, name, profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encryption
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=profile=' + profile] )
        return sstp
    
    def setKeepAliveTimeout(self,name,timeout="30"):
        """
        Method will set keepalive timeout
        :param name:
        :param timeout:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=keepalive-timeout=' + timeout] )
        return sstp

    def enableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=dial-on-demand=yes'] )
        return sstp

    def disableDialOnDemand(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=dial-on-demand=no'] )
        return sstp

    def enableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=add-default-route=yes'] )
        return sstp

    def disableAddDefaultRoute(self,name):
        """
        Method will enable dial on demand
        :param name:
        :return:
        """
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=add-default-route=no'] )
        return sstp

    def setDefRouteDistance(self,name,distance="1"):
        """
        Method will set def route distance
        :param name:
        :param distance:
        :return:
        """
        self.enableAddDefaultRoute(name)
        sstp = self.client.talk( ['/interface/sstp-client/set', '=numbers=' + name, '=default-route-distance=' + distance] )
        return sstp
    
    def setAllow(self,name,auth="mschap2,mschap1,chap,pap"):
        """
        Method will rename iface
        :param name:
        :param auth: mschap2,mschap1,pap,chap
        :return:
        """
        sstp = self.client.talk(['/interface/sstp-client/set','=numbers='+name,'=allow='+auth])
        return sstp