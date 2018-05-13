from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfLsa:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listLsa(self):
        """
        Method will list all LSA
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/lsa/print'])
        if ospf == {}:
            print("No lsa found")
        else:
            for i in ospf:
                print(ospf)
        return ospf