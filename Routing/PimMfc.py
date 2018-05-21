from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimMfc:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listMfc(self):
        """
        Method will list pim neighbors
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mfc/print'] )
        if pim == {}:
            print("no mfc found")
        else:
            print( "Group\tSource\tRp\tIncomming iface\tOutgoing iface" )
            for i in pim:
                #print(pim[i])
                print(pim[i]['group']+"\t"+pim[i]['source']+"\t"+pim[i]['rp']+"\t"+pim[i]['upstream-interface']+"\t"+pim[i]['downstream-interfaces'])
        return pim