from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipNgRoutes:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRoutes(self):
        """
        Method will list all ripng routes
        :return:
        """
        ripng = self.client.talk(['/routing/ripng/route/print'])
        if ripng == {}:
            print("No route found")
        else:
            for i in ripng:
                print(ripng)
        return ripng