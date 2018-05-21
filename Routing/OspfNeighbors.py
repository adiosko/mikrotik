from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfNeighbors:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list neighbors
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/neighbor/print'])
        if ospf == {}:
            print("No neighbor found")
        else:
            print("Instance\trouter id\taddress\tinterface\tstate changes")
            for i in ospf:
                print(ospf[i]['instance']+"\t"+ospf[i]['router-id']+"\t"+ospf[i]['address']+"\t"+ospf[i]['interface']+
                      "\t"+ospf[i]['state-changes'])
        return ospf