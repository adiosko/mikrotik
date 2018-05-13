from tikapy import TikapyClient
from tikapy import TikapySslClient

class accessList:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)


    def listAccessList(self):
        """
        Method will lis taccess lists
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/access-list/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addAccessList(self):
        """
        Method will add access list
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/access-list/add'])
        return wifi

    def removeAccessList(self,number):
        """
        Method will remove access list
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/remove','=numbers='+number] )
        return wifi

    def  enableAccessList(self,number):
        """
        Method will remove access list
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/enable','=numbers='+number] )
        return wifi

    def disableAccessList(self,number):
        """
        Method will remove access list
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/disable','=numbers='+number] )
        return wifi

    def commentAccessList(self,number,comment):
        """
        Method will remove access list
        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/access-list/comment','=numbers='+number,'=comment='+comment] )
        return wifi