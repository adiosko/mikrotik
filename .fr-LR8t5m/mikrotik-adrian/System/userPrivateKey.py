from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UserPrivateKeys:
    def __init__(self,address,username,password):
        self.client = TikapyClient(address,8728)
        self.client.login( username,password )

    def listKeys(self):
        """

        :return:
        """
        user = self.client.talk(['/user/ssh-keys/private/print'])
        for i in user:
            print(user[i])
        return user

    def removeKey(self,number):
        """

        :param number:
        :return:
        """
        user = self.client.talk(['/user/ssh-keys/private/remove','=numbers='+number])
        return user

    def importKey(self,poublicKeyFile,privateKeyFile,user,password):
        """

        :param poublicKeyFile:
        :param privateKeyFile:
        :param user:
        :param password:
        :return:
        """
        user = self.client.talk(['/user/ssh-keys/private/import','=public-key-file='+poublicKeyFile,'=private-key-file='+privateKeyFile,'=passphrase='+password,'=user'+user])
        return user