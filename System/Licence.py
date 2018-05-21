from tikapy import TikapyClient
from tikapy import TikapySslClient

class Licence:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSystemLicence(self):
        """
        Method will print system licence
        :return: list
        """
        licen = self.client.talk(['/system/license/print'])
        print(licen)
        return licen

    def importLicenceKey(self,fileName):
        """
        Method will import licence key to mikrotik
        :param fileName: licence key file
        :return: list of words
        """
        licen = self.client.talk(['/system/license/import','=file-name='+fileName])
        return licen

    def LicenceOutput(self):
        """
        Method will show licence output
        :return: list of words
        """
        licen = self.client.talk(['/system/license/output'])
        print(licen)
        return licen

    def buyNewLicence(self,user,level,payMethod):
        """
        Method will buy new licence for mikrotik
        :param user:  on which username u are buying license
        :param level: 1-6
        :param payMethod:  credit-keys, deposit, prepaid-keys
        :return: list
        """
        licen = self.client.talk(['/system/license/buy-new-key','=user='+user,'=level='+level,'=pay-method='+payMethod])
        return licen


