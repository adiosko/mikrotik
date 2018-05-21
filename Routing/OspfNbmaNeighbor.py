from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfNbmaNeighbor:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNeighbors(self):
        """
        Method will list neighbors for nbma
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/nbma-neighbor/print'])
        if ospf == {}:
            print("No neighbor found")
        else:
            print("Instance\taddress\tpoll interval\tpriority")
            for i in ospf:
                print(ospf[i]['instance']+"\t"+ospf[i]['address']+"\t"+ospf[i]['poll-interval']+"\t"+ospf[i]['priority'])
        return ospf

    def addNeighbor(self):
        """
        Method will add nbma neighbor
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/nbma-neighbor/add'])
        return ospf

    def removeNeighbor(self,number):
        """
        Method will remove neighbor
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/remove','=numbers='+number] )
        return ospf

    def disableNeighbor(self,number):
        """
        Method will disable neighbor
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/disable', '=numbers=' + number] )
        return ospf

    def enableNeighbor(self,number):
        """
        Method will enable neighbor
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/enable', '=numbers=' + number] )
        return ospf

    def commentNeighbor(self,number,comment):
        """
        Method will comment neighbor
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/comment', '=numbers=' + number,'=comment='+comment] )
        return ospf

    def setInstance(self,number,instance="default"):
        """
        Method will set instance
        :param number:
        :param instance:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/set', '=numbers=' + number, '=instance=' + instance] )
        return ospf

    def  setAddress(self,number,address="0.0.0.0"):
        """
        Method will set new address
        :param number:
        :param address:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/set', '=numbers=' + number, '=address=' + address] )
        return ospf

    def setPollInterval(self,number,interval="00:02:00"):
        """
        Method will set poll interval
        :param number:
        :param interval:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/set', '=numbers=' + number, '=poll-interval=' + interval] )
        return ospf

    def setPriority(self,number,priority="0"):
        """
        Method will set new priority
        :param number:
        :param priority:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/nbma-neighbor/set', '=numbers=' + number, '=priority=' + priority] )
        return ospf
