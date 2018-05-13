from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfAreaRanges:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRanges(self):
        """
        Method will list all ranges
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/area/range/print'])
        if ospf == {}:
            print("no range set")
        else:
            print("Area\trange\tcost\tAdvertise")
            for i in ospf:
                print(ospf[i]['area']+"\t"+ospf[i]['range']+"\t"+ospf[i]['cost']+"\t"+ospf[i]['advertise'])
        return ospf

    def addRange(self,area="backbone"):
        """
        Method will add new area range
        :param area:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/area/range/add','=area='+area])
        return ospf

    def removeRange(self,number):
        """
        Method will remove area
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/remove', '=numbers=' + number] )
        return ospf

    def disableRange(self,number):
        """
        Method will disable range
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/disable', '=numbers=' + number] )
        return ospf

    def enableRange(self,number):
        """
        Method will enable range
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/enable', '=numbers=' + number] )
        return ospf

    def commentRange(self,number,comment):
        """
        Method will comment range
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/comment', '=numbers=' + number,'=comment='+comment] )
        return ospf

    def setArea(self,number,area="default"):
        """
        Method will set new area for range
        :param number:
        :param area:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/set', '=numbers=' + number,'=area='+area] )
        return ospf

    def setRange(self,number,range="0.0.0.0/0"):
        """
        Method willset new range
        :param number:
        :param range:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/set', '=numbers=' + number, '=range=' + range] )
        return ospf

    def setCost(self,number,cost="calculated"):
        """
        Method will set new cost
        :param name:
        :param cost: calculated
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/set', '=numbers=' + number, '=cost=' + cost] )
        return ospf

    def setAdvertise(self,number):
        """
        Method will allow advertise
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/set', '=numbers=' + number, '=advertise=yes'] )
        return ospf

    def unsetAdvertise(self, number):
        """
        Method will allow advertise
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/range/set', '=numbers=' + number, '=advertise=no'] )
        return ospf

