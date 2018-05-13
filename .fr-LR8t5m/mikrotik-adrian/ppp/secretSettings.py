from tikapy import TikapyClient
from tikapy import TikapySslClient

class secretSettings:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def setName(self,name,newName):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set','=numbers='+name,'=name='+newName])
        return ppp

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=password=' + password])
        return ppp

    def setService(self,name,service="any"):
        """
        Method will set user service
        :param name:
        :param service: any,async,l2tp,ovpn,pppoe,pptp,sstp
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=service=' + service])
        return ppp

    def setCalledId(self,name,caller):
        """

        :param name:
        :param caller: IP
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=caller-id=' + caller])
        return ppp

    def setProfile(self,name,profile="default"):
        """
        Method will set profile
        :param name:
        :param profile: default,default-encryption
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=profile=' + password])
        return ppp

    def setLocalAddress(self,name,localaddr):
        """
        Method will set local address
        :param name:
        :param localaddr:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=local-address=' + localaddr])
        return ppp

    def setRemoteAddress(self,name,addr):
        """
        Method will set remore address
        :param name:
        :param addr:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=remote-address=' + addr])
        return ppp

    def setRoutes(self,name,routes):
        """
        Method will add routes to profile
        :param name:
        :param routes:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=routes=' + routes])
        return ppp

    def setLimitBytesIn(self,name,limit="0"):
        """
        Method will set limit
        :param name:
        :param limit:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=limit-bytes-in=' + limit])
        return ppp

    def setLimitBytesOut(self,name,limit="0"):
        """
        Method will set limit
        :param name:
        :param limit:
        :return:
        """
        ppp = self.client.talk(['/ppp/secret/set', '=numbers=' + name, '=limit-bytes-out=' + limit])
        return ppp