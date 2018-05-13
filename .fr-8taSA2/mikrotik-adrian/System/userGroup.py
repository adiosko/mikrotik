from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UsersGroup:
    def __init__(self,address,username,password):
        self.client = TikapyClient(address,8728)
        self.client.login( username,password )

    def listGroups(self):
        """

        :return:
        """
        user = self.client.talk(['/user/group/print'])
        for i in user:
            print(user[i])
        return user

    def addGroup(self,name):
        """

        :param name:
        :return:
        """
        user =self.client.talk(['/user/group/add','=name='+name])
        return user

    def removeGroup(self,name):
        """

        :param name:
        :return:
        """
        user =self.client.talk(['/user/group/remove','=numbers='+name])
        return user

    def commentGroup(self,name,comment):
        """

        :param name:
        :param comment:
        :return:
        """
        user = self.client.talk(['/user/group/comment','=numbers='+name,'=comment='+comment])
        return user