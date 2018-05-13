from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipKeys:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listKeys(self):
        """
        Method will list all keys
        :return:
        """
        rip = self.client.talk(['/routing/rip/keys/print'])
        if rip == {}:
            print("no key found")
        else:
            print("Key chain\tKey ID\tKey\tFrom\tTo")
            for i in rip:
                print(rip[i]['chain']+"\t"+rip[i]['key-id']+"\t"+rip[i]['key']+"\t"+rip[i]['from-time']+"\t"+rip[i]['to-date'])
        return rip

    def addKey(self,chain,key,keyId):
        """
        Method will add key
        :param chain: custom or exiting
        :param key: password
        :param keyId: integer value 0 or 1
        :return:
        """
        rip = self.client.talk(['/routing/rip/keys/add','=chain='+chain,'=key='+key,'=key-id='+keyId])
        return rip

    def removeKey(self,number):
        """
        Method will remove key
        :param number:
        :return:
        """
        rip = self.client.talk(['/routing/rip/keys/remove','=numbers='+number])
        return rip

    def setChain(self,number,chain):
        """
        Method will set new chain of existing chain
        :param number:
        :param chain:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number,'=chain='+chain])
        return rip

    def setKeyId(self,number,keyId="0"):
        """
        Method will set key id
        :param number:
        :param id:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number,'=key-id='+keyId])
        return rip

    def setKey(self,number,key):
        """
        Method will chanke password of key
        :param number:
        :param key:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number, '=key=' + key] )
        return rip

    def setFromDate(self,number,time):
        """
        Method will set start date and time of key
        :param number:
        :param time: f.e. Oct/10/2017
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number, '=from-date=' + time] )
        return rip

    def setFromTime(self, number, time):
        """
        Method will set start date and time of key
        :param number:
        :param time: f.e. 00:00:00
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number, '=from-time=' + time] )
        return rip

    def setExpirationDate(self, number, time="forever"):
        """
        Method will set start date and time of key
        :param number:
        :param time: validation day, Feb/02/2018
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number, '=to-date=' + time] )
        return rip

    def setExpirationTime(self, number, time="forever"):
        """
        Method will set start date and time of key
        :param number:
        :param time: validation day, 00:00:00
        :return:
        """
        rip = self.client.talk( ['/routing/rip/keys/set', '=numbers=' + number, '=to-time=' + time] )
        return rip