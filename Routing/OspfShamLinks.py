from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfShamLinks:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listShamLinks(self):
        """
        Method will list sham links
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/sham-link/print'])
        if ospf == {}:
            print("No sham link set")
        else:
            print("Src address\tDst address\tCost\tarea")
            for i in ospf:
                print(ospf[i]['src-address']+"\t"+ospf[i]['dst-address']+"\t"+ospf[i]['cost']+"\t"+ospf[i]['area'])
        return ospf

    def addLink(self,src,dst,area="backbone"):
        """
        Method will add new link
        :param src: src address
        :param dst: dst address
        :param area: area
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/sham-link/add','=src-address='+src,'=dst-address='+dst,'=area='+area])
        return ospf

    def removeLink(self,number):
        """
        Method will remove the link
        :param number:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/sham-link/remove','=numbers='+number])
        return ospf

    def disableLink(self,number):
        """
        Method will disable link
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/disable', '=numbers=' + number] )
        return ospf

    def enableLink(self,number):
        """
        Method will enable link
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/enable', '=numbers=' + number] )
        return ospf

    def commentLink(self,number,comment):
        """
        Method will comment link
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/comment', '=numbers=' + number,'=comment='+comment] )
        return ospf

    def setSrcAddress(self,number,src):
        """
        Method will set src address
        :param number:
        :param src:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/set', '=numbers=' + number, '=src-address=' + src] )
        return ospf

    def setDstAddress(self,number,dst):
        """
        Method will set dst address
        :param number:
        :param dst:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/set', '=numbers=' + number, '=dst-address=' + dst] )
        return ospf

    def setCost(self,number,cost="10"):
        """
        Method will set new cost
        :param number:
        :param cost:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/set', '=numbers=' + number, '=cost=' + cost] )
        return ospf

    def setArea(self,number,area):
        """
        Method will set area
        :param number:
        :param area:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/set', '=numbers=' + number, '=area=' + area] )
        return ospf

    def setCOmment(self,number,comment):
        """
        Method will comment link
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/sham-link/set', '=numbers=' + number, '=comment=' + comment] )
        return ospf


