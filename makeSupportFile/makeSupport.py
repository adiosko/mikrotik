from tikapy import TikapyClient
from tikapy import TikapySslClient

class makeSupport:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def makeSupportFile(self,filename=None):
        """
        Method will create support file
        :param filename: if no name is provided, default name wull be useed
        :return: list
        """
        sup = self.client.talk(['#kod https://wiki.mikrotik.com/wiki/Manual:Support_Output_File'])