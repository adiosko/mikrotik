from tikapy import TikapyClient
from tikapy import TikapySslClient

class securityProfile:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listProfiles(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addProfile(self,name,password):
        """
        Method will add profile
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/add','=name='+name,'=mode=dynamic-keys','=wpa2-pre-shared-key='+password,'=authentication-types=wpa2-psk'])
        return wifi

    def removeProfile(self,name):
        """
        Method will remove profile
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/remove','=numbers='+name])
        return wifi


    def commentProfile(self,name,comment):
        """
        Method will remove profile
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/comment','=numbers='+name,'=comment='+comment])
        return wifi

