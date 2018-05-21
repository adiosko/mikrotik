from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UsersSshKeys:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password )

    def listKeys(self):
        """

        :return:
        """
        user = self.client.talk(['/user/ssh-keys/print'])
        for i in user:
            print(user[i])
        return user

    def removeKey(self,number):
        """

        :param number:
        :return:
        """
        user = self.client.talk(['/user/ssh-keys/remove','=numbers='+number])
        return user

    def importKey(self,keyFile,username):
        """

        :param keyFile:
        :param username:
        :return:
        """
        user = self.client.talk(['/user/ssh-keys/import','=public-key-file='+keyFile,'=user='+username])
        return username

    