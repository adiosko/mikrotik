from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UserActive:
    def __init__(self,address,username,password):
        self.client = TikapyClient(address,8728)
        self.client.login( username,password )

    def listActiveUsers(self):
        """

        :return:
        """
        user = self.client.talk(['/user/active/print'])
        print("Name\tAt\tFrom\tVia\tGroup")
        for i in user:
            print(user[i]['name']+"\t"+user[i]['when']+"\t"+user[i]['address']+"\t"+user[i]['via']+"\t"+user[i]['group'])
        return user