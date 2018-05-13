from tikapy import TikapyClient
from tikapy import TikapySslClient

class SystemMaintenance:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def shutdownRouter(self):
        """
        method will shutdown the mikrotik device
        :return: output of api words
        """
        print("Shutting down the router")
        shutdown = self.client.talk(['/system/shutdown'])
        print(shutdown)
        return shutdown

    def rebootRouter(self):
        """
        method will reboot the router
        :return: api output
        """
        print("Rebooting the router")
        reboot = self.client.talk(['/system/reboot'])
        print(reboot)
        return reboot