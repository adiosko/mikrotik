from tikapy import TikapyClient
from tikapy import TikapySslClient

class Pool:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPools(self):
        """
        Method will list pools
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/print'])
        if pool == {}:
            print("no pool found")
        else:
            print("Name\tPrefix\tlength of prefix")
            for i in pool:
                print(pool[i]['name']+"\t"+pool[i]['prefix']+"\t"+pool[i]['prefix-length'])
        return pool

    def addPool(self,name,prefix,prefixLength):
        """
        Method will add prefix
        :param name:
        :param prefix: ::/0 f.e.
        :param prefixLength: less than 60
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/add','=name='+name,'=prefix='+prefix,'=prefix-length='+prefixLength])
        return pool

    def removePool(self,name):
        """
        Method will remove pool
        :param name:
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/remove','=numbers='+name])
        return pool

    def setPoolName(self,name,NewName):
        """
        Method will set new name
        :param name:
        :param NewName:
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/set','=numbers='+name,'=name='+NewName])
        return pool

    def setPrefix(self,name,prefix):
        """
        Method will set prefix
        :param name:
        :param prefix: ::/0
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/set','=numbers='+name,'=prefix='+prefix])
        return pool

    def setPrefixLength(self,name,prefix):
        """
        Method will set prefix length
        :param name:
        :param prefix: max 60 bits
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/set','=numbers='+name,'=prefix-length='+prefix])
        return pool

    #Used prefixes
    def listUsedPrefixes(self):
        """
        Method will list prefixes
        :return:
        """
        pool = self.client.talk(['/ipv6/pool/used/print'])
        if pool == {}:
            print("No pool found")
        else:
            print("Pool\tPrefix\tOwner\tInfo")
            for i in pool:
                print(pool[i]['name']+"\t"+pool[i]['prefix']+"\t"+pool[i]['owner']+"\t"+pool[i]['info'])
        return pool