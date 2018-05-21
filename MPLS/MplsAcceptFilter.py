from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsLdpAcceptFilter:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listFilter(self):
        """
        Method will list accept filter
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/accept-filter/print'])
        if mpls == {}:
            print("No filter found")
        else:
            print("Prefix\tNeighbor\tAccept")
            for i in mpls:
                print(mpls[i]['prefix']+"\t"+mpls[i]['neighbor']+"\t"+mpls[i]['accept'])
        return mpls

    def addFilter(self):
        """
        Method will add  filter
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/accept-filter/add'])
        return mpls

    def removeFilter(self,number):
        """
        Method will remove filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/remove','=numbers='+number] )
        return mpls

    def enableFilter(self,number):
        """
        Method will enable filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/enable', '=numbers=' + number] )
        return mpls

    def disableFilter(self,number):
        """
        Method will disable filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/disable', '=numbers=' + number] )
        return mpls

    def commentFilter(self,number,comment):
        """
        Method will comment filter
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/comment', '=numbers=' + number,'=comment='+comment] )
        return mpls

    def setPrefix(self,number,prefix="0.0.0.0/0"):
        """
        Method will set prefix
        :param number:
        :param prefix: subnet/prefix
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/set', '=numbers=' + number, '=prefix=' + prefix] )
        return mpls

    def setNeighbor(self,number,neighbor):
        """
        Method will set enighbor IP
        :param number:
        :param neighbor:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/set', '=numbers=' + number, '=neighbor=' + neighbor] )
        return mpls

    def acceptRule(self,number):
        """
        Method will accept the rule
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/set', '=numbers=' + number, '=accept=yes'] )
        return mpls

    def denyRule(self,number):
        """
        Method will deny rule
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/accept-filter/set', '=numbers=' + number, '=accept=no'] )
        return mpls



