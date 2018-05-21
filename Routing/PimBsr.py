from tikapy import TikapyClient
from tikapy import TikapySslClient

class BsrStats:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listBsr(self):
        """
        Method will list bsr connections
        :return:
        """
        pim = self.client.talk( ['/routing/pim/bsr/print'] )
        if pim == {}:
            print("NO bsr found")
        else:
            print("Zone type\tBsr address\tscope zone\tbsr-priority\tlocal address")
            for i in pim:
                print(pim[i]['zone-type']+"\t"+pim[i]['bsr-address']+"\t"+pim[i]['scope-zone']+"\t"+pim[i]['bsr-priority']+"\t"+pim[i]['local-address'])
        return pim