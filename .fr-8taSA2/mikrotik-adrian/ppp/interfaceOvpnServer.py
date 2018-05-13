from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfaceOvpnServer:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def enable(self):
        """
        Method will enable server
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set','=enabled=yes'])
        return ppp

    def disable(self):
        """
        Method will disable ovpn server
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=enabled=no'])
        return ppp

    def setPort(self,port="1194"):
        """
        Method will set port
        :param port:
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=port='+port])
        return ppp

    def setMode(self,mode="ip"):
        """
        Method will set mode
        :param mode: ip,ethernet
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=mode='+mode])
        return ppp
    
    def setNetmask(self,netmask="24"):
        """
        Method will set netmask
        :param netmask: 
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=netmask='+netmask])
        return ppp
    
    def setMacAddress(self,mac):
        """
        Method will set mac address
        :param mac: 
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=mac-address='+mac])
        return ppp
    
    def setMaxMtu(self,mtu="1500"):
        """
        Method will set max mtu
        :param mtu: 
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=max-mtu='+mtu])
        return ppp
    
    def setKeepaliveTimeout(self,timeout="60"):
        """
        Method will set timeoyut
        :param timeout: 
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=keepalive-timeout='+timeout])
        return ppp
    
    def setProfile(self,profile="default"):
        """
        Method will set profile
        :param profile: default,default-encrypt
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=default-profile='+profile])
        return ppp
    
    def setCertificate(self,cert):
        """
        Method will set cert
        :param cert: 
        :return: 
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=certificate='+cert])
        return ppp

    def requiereClientCert(self):
        """
        Method will requiere client cert
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=require-client-certificate=yes'])
        return ppp

    def unrequiereClientCert(self):
        """
        Method will requiere client cert
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=require-client-certificate=no'])
        return ppp

    def setAUthentication(self,auth="md5,sha1"):
        """
        Method will set autj
        :param auth: md5,sha1,null
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=auth='+auth])
        return ppp

    def setCipher(self,ciph="blowfish128,aes128"):
        """
        Method will set cipher
        :param ciph: aes128,aes192,aes256,blowfish128,null
        :return:
        """
        ppp = self.client.talk(['/interface/ovpn-server/server/set', '=cipher='+ciph])
        return ppp