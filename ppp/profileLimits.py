from tikapy import TikapyClient
from tikapy import TikapySslClient

class profileLimits:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setSessionTimeout(self,name,timeout="00:00:00"):
        """
        Method will setsession timeout
        :param name:
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=session-timeout='+timeout])
        return ppp

    def setIdleTimeout(self,name,timeout="00:00:00"):
        """
        Method willset idle timeout
        :param name:
        :param timeout:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=idle-timeout=' + timeout])
        return ppp

    def setRateLimit(self,name,tx,rx):
        """
        Method will set rate limit tx/rx
        :param name:
        :param tx:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=rate-limit='+tx+"/"+rx])
        return ppp

    def setOnlyOne(self,name,onlyone="default"):
        """
        Method will set only one
        :param name:
        :param onlyone: no,yes,default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=only-one=' + onlyone])
        return ppp