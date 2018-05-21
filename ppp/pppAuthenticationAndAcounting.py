from tikapy import TikapyClient
from tikapy import TikapySslClient

class pppAuthenticationAndAcounting:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def useRadius(self):
        """
        Method will enable radius
        :return:
        """
        ppp = self.client.talk(['/ppp/aaa/set','=use-radius=yes'])
        return ppp

    def useAccounting(self):
        """
        Method will enable accounting
        :return:
        """
        ppp = self.client.talk(['/ppp/aaa/set','=accounting=yes'])
        return ppp

    def useCircuitIdInNasPortId(self):
        """
        Method will enable
        :return:
        """
        ppp = self.client.talk(['/ppp/aaa/set','=use-circuit-id-in-nas-port-id=yes'])
        return ppp

    def setInterimUpdate(self,update="00:00:00"):
        """
        method will set interim update interval
        :param update:
        :return:
        """
        ppp = self.client.talk(['/ppp/aaa/set','=interim-update='+update])
        return ppp