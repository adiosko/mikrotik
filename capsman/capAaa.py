from tikapy import TikapyClient
from tikapy import TikapySslClient

class capAaa:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setMacFormat(self,format="XX:XX:XX:XX:XX:XX"):
        """

        :param format:
        :return:
        """
        wifi = self.client.talk(['/caps-man/aaa/set','=mac-format='+format])
        return wifi

    def setMacMode(self,mode="as-username"):
        """

        :param mode: as-username,as-username-and-password
        :return:
        """
        wifi = self.client.talk(['/caps-man/aaa/set', '=mac-mode=' + mode])
        return wifi

    def setMacCaching(self,caching="00:00:00"):
        """

        :param caching:
        :return:
        """
        wifi = self.client.talk(['/caps-man/aaa/set', '=mac-caching=' +caching])
        return wifi

    def setInterimUpdate(self,update="00:00:00"):
        """

        :param update:
        :return:
        """
        wifi = self.client.talk(['/caps-man/aaa/set', '=interim-update=' + update])
        return wifi