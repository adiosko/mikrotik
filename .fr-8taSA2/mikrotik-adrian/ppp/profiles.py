from tikapy import TikapyClient
from tikapy import TikapySslClient

class profiles:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listProfiles(self):
        """
        Method will list profiles
        :return:
        """
        ppp =self.client.talk(['/ppp/profile/print'])
        print("Name\tLocal address\tRemote address")
        for i in ppp:
            print(ppp[i]['name']+"\t"+ppp[i]['local-address']+"\t"+ppp[i]['remote-address'])
        return ppp

    def addProfile(self,name,localaddr,remaddr):
        """
        Method will add new profiles
        :param name:
        :param localaddr:
        :param remaddr:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/add','=name='+name,'=local-address='+localaddr,'=remote-address='+remaddr])
        return ppp

    def removeProfile(self,name):
        """
        Method will remove profile
        :param name:
        :return:
        """
        ppp =self.client.talk(['/ppp/profile/remove','=numbers='+name])
        return ppp

    def commentProfile(self,name,comment):
        """
        Methdo will comment profile
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/comment','=numbers='+name,'=comment='+comment])
        return ppp




