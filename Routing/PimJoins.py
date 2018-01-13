from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimJoins:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listJoins(self):
        """
        Method will list pim joins
        :return:
        """
        pim = self.client.talk( ['/routing/pim/join/print'] )
        if pim == {}:
            print("no join found")
        else:
            print( "Group\tSource\tRp\tJoin state\tJoin registration state" )
            for i in pim:
                #print(pim[i])
                print(pim[i]['group']+"\t"+pim[i]['source']+"\t"+pim[i]['rp']+"\t"+pim[i]['join-state']+"\t"+pim[i]['joined'])
        return pim