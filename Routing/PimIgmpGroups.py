from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimIgmpGroups:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listGroups(self):
        """
        Method will list pim joins
        :return:
        """
        pim = self.client.talk( ['/routing/pim/igmp-group/print'] )
        if pim == {}:
            print("no group found")
        else:
            print( "Group\tSource\tRp" )
            for i in pim:
                #print(pim[i])
                print(pim[i]['group']+"\t"+pim[i]['source']+"\t"+pim[i]['last-reported'])
        return pim