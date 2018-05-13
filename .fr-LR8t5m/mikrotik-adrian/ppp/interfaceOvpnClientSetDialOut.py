from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceOvpnClientSetDialOut:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setConnectTo(self, name, conect):
        """

        :param name:
        :param conect:
        :return:
        """
        sstp = self.client.talk( ['/interface/ovpn-client/set', '=numbers=' + name, '=connect-to' + conect] )
        return sstp
    
    def setPort(self,name,port="1194"):
        """
        Method will set port
        :param port:
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name, '=port='+port])
        return ovpn

    def setMode(self,name,mode="ip"):
        """
        Method will set mode
        :param mode: ip,ethernet
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name,'=mode='+mode])
        return ovpn

    def setUser(self,name,user):
        """
        Method will set port
        :param port:
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name, '=user='+user])
        return ovpn

    def setPassword(self,name,password):
        """
        Method will set port
        :param password:
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name, '=password='+password])
        return ovpn

    def setProfile(self,name,profile="default"):
        """
        Method will set port
        :param profile: default,default-encryption
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name, '=profile='+profile])
        return ovpn

    def setCertificate(self,name,certificate="none"):
        """
        Method will set port
        :param certificate: none,certName
        :return:
        """
        ovpn = self.client.talk(['/interface/ovpn-client/set','=numbers='+name, '=certificate='+certificate])
        return ovpn

    def setAuthentication(self,name,auth="sha1"):
        """
        Method will set authentication
        :param name:
        :param auth: sha1,null,md5
        :return:
        """
        ovpn = self.client.talk( ['/interface/ovpn-client/set', '=numbers=' + name, '=auth=' + auth] )
        return ovpn


    def setCipher(self,name,cipher="blowfish128"):
        """
        Method will set authentication
        :param name:
        :param cipher: blowfish128,aes128,aes192,aes256,null
        :return:
        """
        ovpn = self.client.talk( ['/interface/ovpn-client/set', '=numbers=' + name, '=cipher=' + cipher] )
        return ovpn

    def addDefaultRoute(self,name):
        """
        Method will add default route
        :param name:
        :return:
        """
        ovpn = self.client.talk( ['/interface/ovpn-client/set', '=numbers=' + name, '=add-default-route=yes'] )
        return ovpn

    def notAddDefaultRoute(self,name):
        """
        Method will add default route
        :param name:
        :return:
        """
        ovpn = self.client.talk( ['/interface/ovpn-client/set', '=numbers=' + name, '=add-default-route=no'] )
        return ovpn