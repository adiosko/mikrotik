from tikapy import TikapyClient
from tikapy import TikapySslClient

class MeshPorts:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPorts(self):
        """
        Method will list mesh ports
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/port/print'])
        print("Interface\tMesh")
        for i in mesh:
            print(mesh[i]['interface']+"\t"+mesh[i]['mesh'])
        return mesh

    def addPort(self,interface,mesh):
        """
        Method will add port
        :param interface:
        :param mesh:
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/port/add','=interface='+interface,'=mesh='+mesh])
        return mesh

    def removePort(self,number):
        """
        Method will remove port
        :param number:
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/port/remove','=numbers='+number])
        return mesh

    def enablePort(self,number):
        """
        Method will enable port
        :param number:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/enable', '=numbers=' + number] )
        return mesh

    def disablePort(self,number):
        """
        Method will disable port
        :param number:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/disable', '=numbers=' + number] )
        return mesh

    def commentPort(self,number,comment):
        """
        Method will comment port
        :param number:
        :param comment:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/comment', '=numbers=' + number,'=comment='+comment] )
        return mesh

    def setInterface(self,number,interface):
        """
        Method will set interface
        :param number:
        :param interface:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/set', '=numbers=' + number, '=interface=' + interface] )
        return mesh

    def setMesh(self,number,mesh):
        """
        Method will set mesh
        :param number:
        :param mesh: mesh created in mesh class
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/set', '=numbers=' + number, '=mesh=' + mesh] )
        return mesh

    def setPathCost(self,number,cost="10"):
        """
        Method will set parh cost of port
        :param number:
        :param cost:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/set', '=numbers=' + number, '=path-cost=' + cost] )
        return mesh

    def setHelloInterval(self,number,interval="10"):
        """
        Method will set hello interval in secs
        :param number:
        :param interval:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/set', '=numbers=' + number, '=hello-interval=' + interval] )
        return mesh

    def setPortType(self,number,port="auto"):
        """
        Method will set port type
        :param number:
        :param port: auto,ethernet,wireless,WDS
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/port/set', '=numbers=' + number, '=port-type=' + port] )
        return mesh
