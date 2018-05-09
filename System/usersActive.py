from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UserActive:
    def __init__(self,address,username,password):
        self.client = TikapySslClient(address,8729)
        self.client.login( username,password )

    def listActiveUsers(self):
        """

        :return:
        """
        user = self.client.talk(['/user/active/print'])
        return user