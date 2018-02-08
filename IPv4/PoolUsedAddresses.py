from tikapy import TikapyClient
from tikapy import TikapySslClient

class PoolUsedAddresses:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listAddresses(self):
        """
        Method will list used pool addresses
        :return:
        """
        pool = self.client.talk(['/ip/pool/used/print'])
        print("Pool\tAddress\tOwner\tInfo")
        for i in pool:
            print(pool[i]['pool']+"\t"+pool[i]['address']+"\t"+pool[i]['owner']+"\t"+pool[i]['info'])
        return pool