from tikapy import TikapyClient
from tikapy import TikapySslClient

class securityProfileSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setName(self,name,newName):
        """
        Method wil lrename profile
        :param name:
        :param newName:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=name='+newName])
        return wifi

    def setMode(self,name,mode="none"):
        """
        Method will set mode
        :param name:
        :param mode:none,static-keys-optional,static-keys-required
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=mode='+mode])
        return wifi

    def setDynamicKeysMode(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=mode=dynamic-keys'])
        return wifi

    def setAuthenticationTypes(self,name,auth="wpa2-psk"):
        """
        Method will set authentication types
        :param name:
        :param auth:wpa-eap,wpa-psk,wpa2-eap,wpa2-psk
        :return:
        """
        self.setDynamicKeysMode(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=authentication-types='+auth])
        return wifi

    def setUnicastCipher(self,name,cipher="aes-com"):
        """
        Method will set unicast cipher
        :param name:
        :param cipher: aes-com,tkip
        :return:
        """
        self.setDynamicKeysMode(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=unicast-ciphers='+cipher])
        return wifi

    def setGroupCiphers(self,name,cipher="aes-com"):
        """
        Method will set group cipher
        :param name:
        :param cipher: aes-com,tkip
        :return:
        """
        self.setDynamicKeysMode(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=group-ciphers='+cipher])
        return wifi

    def enableWpaPsk(self,name):
        """
        Method will set wpa psk
        :param name:
        :return:
        """
        self.setDynamicKeysMode(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=authentication-types=wpa-psk'])
        return wifi

    def enableWpa2Psk(self,name):
        """
        Method will enable wpa2 psk
        :param name:
        :return:
        """
        self.setDynamicKeysMode( name )
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=authentication-types=wpa2-psk'] )
        return wifi

    def setWpaPresharedKey(self,name,password):
        """

        :param name:
        :param password:
        :return:
        """
        self.setDynamicKeysMode(name)
        self.enableWpaPsk(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set', '=numbers=' + name, '=wpa-pre-shared-key=' + password] )
        return wifi

    def setWpa2Psk(self,name,password):
        """
        Method will set wpa2 psk
        :param name:
        :param password:
        :return:
        """
        self.setDynamicKeysMode( name )
        self.enableWpaPsk( name )
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=wpa2-pre-shared-key=' + password] )
        return wifi

    def setGroupKeyUpdate(self,name,group="00:05:00"):
        """
        Method will set group key update
        :param name:
        :param group:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=group-key-update='+group])
        return wifi

    def enableManagementProtection(self,name,mode="allowed"):
        """
        Metho will enable management protection
        :param name:
        :param mode: allowed,required
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=management-protection=' + mode] )
        return wifi

    def disableManagementProtection(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=management-protection=disabled'] )
        return wifi

    def setManagementProtectionKey(self,name,password):
        """
        Method wil lset mgmt key
        :param name:
        :param password:
        :return:
        """
        self.enableManagementProtection(name)
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=management-protection-key='+password])
        return wifi

    def enableEap(self,name):
        """
        Method will enable wpa2 psk
        :param name:
        :return:
        """
        self.setDynamicKeysMode( name )
        wifi = self.client.talk(
            ['/interface/wireless/security-profiles/set', '=numbers=' + name, '=authentication-types=wpa2-eap,wpa-eap'] )
        return wifi

    def enableStaticKeyOptional(self,name):
        """

        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/set','=numbers='+name,'=mode=static-keys-optional'])
        return wifi