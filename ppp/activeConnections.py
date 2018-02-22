from tikapy import TikapyClient
from tikapy import TikapySslClient

class activeCOnnections:
    def __init__(self, address, username, password):
        self.client = TikapyClient(address, 8728)
        self.client.login(username, password)

    def listConnections(self):
        """
        Method will list connections
        :return:
        """
        ppp = self.client.talk(['/ppp/active/print'])
        print("Name\tService\tCallerID\tEncoding\tAddress\tUptime")
        for i in ppp:
            print(ppp[i]['name']+"\t"+ppp[i]['service']+"\t"+ppp[i]['caller-id']+"\t"+ppp[i]['encoding']+"\t"+ppp[i]['address']+"\t"+ppp[i]['uptime'])
        return ppp

    def removeConnection(self,name):
        """
        Method will remove connection
        :param name:
        :return:
        """
        ppp = self.client.talk(['/ppp/active/remove','=numbers='+name])
        return ppp