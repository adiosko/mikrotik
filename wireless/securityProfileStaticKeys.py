from tikapy import TikapyClient
from tikapy import TikapySslClient
from wireless import securityProfileSetGeneral

class securityProfileSetStaticKeys:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setKey0(self,name,keyValue,value):
        """
        Method wil lset value
        :param name:
        :param keyValue: none,40-bit-wep,104bit-wep,aes-com,none,tkip
        :param value: hexa value
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=static-algo0='+keyValue,'=static-key-0='+value])
        return wifi

    def setKey1(self,name,keyValue,value):
        """
        Method wil lset value
        :param name:
        :param keyValue: none,40-bit-wep,104bit-wep,aes-com,none,tkip
        :param value: hexa value
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=static-algo1='+keyValue,'=static-key-1='+value])
        return wifi

    def setKey2(self,name,keyValue,value):
        """
        Method wil lset value
        :param name:
        :param keyValue: none,40-bit-wep,104bit-wep,aes-com,none,tkip
        :param value: hexa value
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=static-algo2='+keyValue,'=static-key-2='+value])
        return wifi

    def setKey3(self,name,keyValue,value):
        """
        Method wil lset value
        :param name:
        :param keyValue: none,40-bit-wep,104bit-wep,aes-com,none,tkip
        :param value: hexa value
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=static-algo3='+keyValue,'=static-key-3='+value])
        return wifi

    def setTransmitKey(self,name,key="key-0"):
        """

        :param name:
        :param key:key-0,key-1,key-2,key-3
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=static-transmit-key='+key] )
        return wifi

    def setPrivateKey(self,name,algo,value):
        """
        Method will set private key
        :param name:
        :param algo:
        :param value:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profile/set','=numbers='+name,'=static-sta-private-algo='+algo,'=static-sta-private-key='+value])
        return wifi