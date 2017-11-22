from tikapy import TikapyClient
from tikapy import TikapySslClient

class Health:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listSystemHealth(self):
        """
        Method will list all system health info not aplicable on API
        :return:
        """
        helth = self.client.talk(['/system/health/print'])
        print(helth)
        return helth

    def enableAfterReboot(self):
        """
        Method will enable system health checking after the reboot
        :return: list
        """
        helth = self.client.talk(['/system/health/set','=state-after-reboot=enabled'])
        return helth

    def disableAfterReboot(self):
        """
        Method will disable health checking after reboot
        :return: list
        """
        helth = self.client.talk( ['/system/health/set', '=state-after-reboot=disabled'] )
        return helth