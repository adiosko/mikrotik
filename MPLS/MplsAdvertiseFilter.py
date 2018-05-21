from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsAdvertiseFilter:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listFilters(self):
        """
        Method will list filters
        :return:
        """
        mpls = self.client.talk(['/mpls/ldp/advertise-filter/print'])
        if mpls == {}:
            print("No filter found")
        else:
            print("Prefix\tNeighbor\tAdvertise")
            for i in mpls:
                print(mpls[i]['prefix']+"\t"+mpls[i]['neighbor']+"\t"+mpls[i]['advertise'])
        return mpls

    def addFilter(self):
        """
        Method will ad filter
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/add'] )
        return mpls

    def removeFilter(self,number):
        """
        Method will remove filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/remove','=numbers='+number] )
        return mpls

    def enableFilter(self,number):
        """
        Method will enable filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/enable', '=numbers=' + number] )
        return mpls

    def disableFilter(self,number):
        """
        Method will disable filter
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/disable', '=numbers=' + number] )
        return mpls

    def commentFilter(self,number,comment):
        """
        Method will comment filter
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/comment', '=numbers=' + number,'=comment='+comment] )
        return mpls

    def setPrefix(self,number,prefix="0.0.0.0/0"):
        """
        Method will set prefix
        :param number:
        :param prefix: subnet/prefix
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/set', '=numbers=' + number,'=prefix='+prefix] )
        return mpls

    def setNeighbor(self,number,neighbor):
        """
        Method will set neighbor
        :param number:
        :param neighbor: IP
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/set', '=numbers=' + number,'=neighbor='+neighbor] )
        return mpls

    def advertiseRule(self,number):
        """
        Method will advertise rule
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/set', '=numbers=' + number,'=advertise=yes'] )
        return mpls

    def doNotAdvertiseRule(self,number):
        """
        Method will deny advertise
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/ldp/advertise-filter/set', '=numbers=' + number,'=advertise=no'] )
        return mpls