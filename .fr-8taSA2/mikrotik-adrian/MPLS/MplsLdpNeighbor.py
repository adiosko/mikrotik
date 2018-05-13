from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsLdpNeighbors:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list neighbors
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/neighbor/print'])
        if mpls == {}:
            print("no neighbor found")
        else:
            print("Transport\tsend targetted\tdynamic status")
            for i in mpls:
                print(mpls[i]['transport']+"\t"+mpls[i]['send-targeted']+"\t"+mpls[i]['dynamic'])
        return mpls

    def addNeighbor(self,neighbor):
        """
        Method will add neighbor by IP
        :param neighbor: IP
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/neighbor/add','=transport='+neighbor])
        return mpls

    def removeNeighbor(self,number):
        """
        Method will remove neighbor
        :param number:
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/neighbor/remove','=numbers='+number])
        return mpls

    def enableNeighbor(self,number):
        """
        Method will enable neighbor
        :param number:
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/neighbor/enable','=numbers='+number])
        return mpls

    def disableNeighbor(self,number):
        """
        Method will disable neighbor
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/neighbor/disable', '=numbers=' + number] )
        return mpls

    def commentNeighbor(self,number,comment):
        """
        Method will comment neighbor
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/neighbor/comment', '=numbers=' + number,'=comment='+comment] )
        return mpls

    def setTransport(self,number,transport):
        """
        Method will set transport address
        :param number:
        :param transport:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/neighbor/set', '=numbers=' + number,'=transport='+transport] )
        return mpls

    def sendTargetted(self,number):
        """
        Method will send trageted transport IP
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/neighbor/set', '=numbers=' + number,'=send-targeted=yes'] )
        return mpls
