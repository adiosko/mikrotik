from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimRp:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listPimRp(self):
        """
        Method will list rps
        :return:
        """
        pim = self.client.talk(['/routing/pim/rp/print'])
        if pim == {}:
            print("no rp found")
        else:
            print("address\tgroup\tpriority\tactive-groups")
            for i in pim:
                print(pim[i]['address']+"\t"+pim[i]['group']+"\t"+pim['priority']+"\t"+pim[i]['active-groups'])
        return pim

    def addRp(self,address):
        """
        Method will add pim based on address/prefix
        :param address:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/add','=address='+address] )
        return pim

    def removeRp(self,number):
        """
        Method will remove rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/remove', '=numbers=' + number] )
        return pim

    def enableRp(self,number):
        """
        Method will enable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/enable', '=numbers=' + number] )
        return pim

    def disableRp(self,number):
        """
        Method will disable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/disable', '=numbers=' + number] )
        return pim

    def commentRp(self,number,comment):
        """
        Method will comment rp
        :param number:
        :param comment:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/comment', '=numbers=' + number,'=comment='+comment] )
        return pim

    def setAddress(self,number,address):
        """
        Method will set rp address
        :param number:
        :param address:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/set', '=numbers=' + number,'=address='+address] )
        return pim

    def setGroup(self,number,group="224.0.0.0/4"):
        """
        Method will set group
        :param number:
        :param group:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/set', '=numbers=' + number, '=group=' + group] )
        return pim

    def setPriority(self,number,priority="192"):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/set', '=numbers=' + number, '=priority=' + priority] )
        return pim

    def setHashMaskLength(self,number,hashin="30"):
        """
        Method willset hash amsk length
        :param number:
        :param hash:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp/set', '=numbers=' + number, '=hash-mask-length=' + hashin] )
        return pim