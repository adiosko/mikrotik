from tikapy import TikapyClient
from tikapy import TikapySslClient

class secrets:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def listSecrets(self):
        """
        Method will list secrets
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/print'])
        print("Name\tPassword\tService\tProfile")
        for i in ppp:
            print(ppp[i]['name']+"\t"+ppp[i]['password']+"\t"+ppp[i]['service']+"\t"+ppp[i]['profile'])
        return ppp

    def addSecret(self,name,password,profile="default"):
        """
        Method will add secret
        :param name:
        :param password:
        :param profile: ppp profile
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/add','=name='+name,'=password='+password,'=profile='+profile])
        return ppp

    def removeSecret(self,name):
        """
        Method will remove secret
        :param name:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/remove','=numbers='+name])
        return ppp

    def enableSecret(self,name):
        """
        Method will enbale secret
        :param name:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/enable', '=numbers=' + name])
        return ppp

    def disableSecret(self,name):
        """
        Method will disable secret
        :param name:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/disable', '=numbers=' + name])
        return ppp

    def commentSecret(self,name,comment):
        """
        Method will comment secret
        :param name:
        :param comment:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/comment', '=numbers=' + name,'=comment='+comment])
        return ppp
