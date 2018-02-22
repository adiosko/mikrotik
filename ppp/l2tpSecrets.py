from tikapy import TikapyClient
from tikapy import TikapySslClient

class l2tpSecrets:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listSecrets(self):
        ppp = self.client.talk(['/ppp/l2tp-secret/print'])
        print("Address\tSecret")
        for i in ppp:
            print(ppp[i]['address'] + "\t" + ppp[i]['secret'])
        return ppp

    def addSecret(self, secret,address="0.0.0.0/0"):
        """
        Mehtod will add secret
        :param address:
        :param secret:
        :return:
        """
        ppp = self.client.talk(['/ppp/l2tp-secret/add', '=address=' + address, '=secret=' + secret])
        return ppp

    def removeSecret(self,number):
        """
        Method will remvoe secret
        :param number:
        :return:
        """
        ppp = self.client.talk(['/ppp/l2tp-secret/remove','=numbers='+number])
        return ppp

    def commentSecret(self,number,comment):
        """
        Method will comment secret
        :param number:
        :param comment:
        :return:
        """
        ppp = self.client.talk(['/ppp/l2tp-secret/comment', '=numbers=' + number,'=comment='+comment])
        return ppp

    def setAddress(self,number,adddress):
        """
        Method will set address
        :param number:
        :param adddress:
        :return:
        """
        ppp = self.client.talk(['/ppp/l2tp-secret/set', '=numbers=' + number, '=address=' + adddress])
        return ppp

    def setSecret(self,number,secret):
        """
        Method will set secret
        :param number:
        :param secret:
        :return:
        """
        ppp = self.client.talk(['/ppp/l2tp-secret/set', '=numbers=' + number, '=secret=' + secret])
        return ppp


