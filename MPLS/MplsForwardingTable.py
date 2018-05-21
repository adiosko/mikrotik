from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsForwardingTable:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listTable(self):
        """
        Method will list forwarding table
        :return:
        """
        mpls = self.client.talk(['/mpls/forwarding-table/print'])
        if mpls == {}:
            print("No entry found")
        else:
            print("In-label\tBytes\tPackets")
            for i in mpls:
                print(mpls[i]['in-label']+"\t"+mpls[i]['bytes']+"\t"+mpls[i]['packets'])
        return mpls