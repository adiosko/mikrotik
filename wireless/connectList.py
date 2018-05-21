from tikapy import TikapyClient
from tikapy import TikapySslClient

class connectList:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listLists(self):
        """

        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/print'])
        for i in wifi:
            print(wifi[i])
        return wifi

    def addList(self,interface):
        """

        :param interface:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/add','=interface='+interface])
        return wifi

    def removeList(self,number):
        """
        Method will remove list
        :param number:
        :return:
        """
        wifi = self.client.talk(['/interface/wireless/connect-list/remove','=numbers='+number])
        return wifi

    def enableList(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/connect-list/enable', '=numbers=' + number] )
        return wifi

    def disableLIst(self,number):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/connect-list/disable', '=numbers=' + number] )
        return wifi

    def commentList(self,number,comment):
        """

        :param number:
        :return:
        """
        wifi = self.client.talk( ['/interface/wireless/connect-list/comment', '=numbers=' + number,'=comment='+comment] )
        return wifi