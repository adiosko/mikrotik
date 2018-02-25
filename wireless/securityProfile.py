from tikapy import TikapyClient
from tikapy import TikapySslClient

class securityProfile:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listProfiles(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addProfile(self,name):
        """
        Method will add profile
        :param name:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/security-profiles/add','=name='+name])
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

