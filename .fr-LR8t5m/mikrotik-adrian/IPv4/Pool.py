from tikapy import TikapyClient
from tikapy import TikapySslClient

class Pool:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPool(self):
        """
        Method will list ip pool
        :return:
        """
        pool = self.client.talk(['/ip/pool/print'])
        return pool

    def addPool(self,name,addressRangeSubnet):
        """
        Method will add pool range
        :param name:
        :param addressRangeSubnet: i.e. 10.0.0.2-10.0.0.254
        :return:
        """
        pool = self.client.talk(['/ip/pool/add','=name='+name,'=ranges='+addressRangeSubnet])
        return pool

    def removePool(self,name):
        """
        Method will remove pool
        :param name:
        :return:
        """
        pool = self.client.talk(['/ip/pool/remove','=numbers='+name])
        return pool

    def setName(self,name,newNAme):
        """
        Method will rename pool
        :param name:
        :param newNAme:
        :return:
        """
        pool = self.client.talk(['/ip/pool/set','=numbers='+name,'=name='+newNAme])
        return pool

    def setRange(self,name,rangeSUbnet):
        """
        Method will set range subnet
        :param name:
        :param rangeSUbnet: i.e. 10.0.0.2-10.0.0.254
        :return:
        """
        pool = self.client.talk(['/ip/pool/set','=numbers='+name,'=ranges='+rangeSUbnet])
        return pool

    def setNextPool(self,name,pool="none"):
        """
        Method will set next pool
        :param name:
        :param pool:
        :return:
        """
        pool = self.client.talk(['/ip/pool/set','=numbers='+name,'=next-pool='+pool])
        return pool