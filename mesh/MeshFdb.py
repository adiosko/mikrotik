from tikapy import TikapyClient
from tikapy import TikapySslClient

class MeshFdb:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listFdb(self):
        """
        Method will list fdb
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/fdb/print'])
        print("Mesh\ttype\tage")
        for i in mesh:
            print(mesh[i]['mesh']+"\t"+mesh[i]['type']+"\t"+mesh[i]['age'])
        return mesh
