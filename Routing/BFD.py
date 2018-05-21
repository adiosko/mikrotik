from tikapy import TikapyClient
from tikapy import TikapySslClient

class BFD:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listBfdInterfaces(self):
        """
        Method will list all bfd interfaces
        :return:
        """
        bfd = self.client.talk(['/routing/bfd/interface/print'])
        if bfd == {}:
            print("No bfd interface set")
        else:
            print( "Interface\tInterval\tMin rx\tMultiplier" )
            for i in bfd:
                print(bfd[i]['interface']+"\t"+bfd[i]['interval']+"\t"+bfd[i]['min-rx']+"\t"
                      +bfd[i]['multiplier'])
        return bfd

    def addBfdInterface(self,interface):
        """
        Method will add bfd interface
        :param interface: interface physica or logical
        :return:
        """
        bfd = self.client.talk(['/routing/bfd/interface/add','=interface='+interface])
        return bfd

    def removeBfdInterface(self,interface):
        """
        Method will remove bfd interface by its order no
        :param interface:
        :return:
        """
        bfd = self.client.talk(['/routing/bfd/interface/remove','=numbers='+interface])
        return bfd

    def enableBfdInterface(self,interface):
        """
        Method will
        :param interface: interface or number
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/interface/enable', '=numbers=' + interface] )
        return bfd

    def disableBfdInterface(self,interface):
        """
        Method will disable interface
        :param interface:
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/interface/disable', '=numbers=' + interface] )
        return bfd

    def setnterfaceMultiplier(self,interface,multiplier="5"):
        """
        Method will set interface multiplier
        :param interface: interface or number
        :param multiplier: number def 5
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/interface/set', '=numbers='+interface,'=multiplier='+multiplier] )
        return bfd

    def setMinimalBfdRx(self,interface,rx="0.200"):
        """
        Method will set minimal bfd rx
        :param interface:
        :param rx: 0.200 s
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/interface/set', '=numbers=' + interface, '=min-rx=' + rx] )
        return bfd

    def setBfdInterval(self,interface,interval="0.200"):
        """
        Method will set BFD interval
        :param interface:
        :param interval: 0.200 s
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/interface/set', '=numbers=' + interface, '=interval=' + interval] )
        return bfd

    def listBfdNeighbors(self):
        """
        Method will list all bfd neighbors
        :return:
        """
        bfd = self.client.talk( ['/routing/bfd/neighbor/print'] )
        if bfd == {}:
            print("No neighbor found")
        else:
            print(bfd)
        return bfd