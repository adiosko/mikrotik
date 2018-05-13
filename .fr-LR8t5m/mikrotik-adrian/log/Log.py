from tikapy import TikapyClient
from tikapy import TikapySslClient

class Log:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address,8729)
        self.client.login( username,password)

    def listLog(self):
        """
        Method will print log
        :return:
        """
        log = self.client.talk(['/log/print'])
        return log
