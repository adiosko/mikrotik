from tikapy import TikapyClient
from tikapy import TikapySslClient

class RoutingFilters:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listFilters(self):
        """
        Method will list filters
        :return:
        """
        filt = self.client.talk(['/routing/filter/print'])
        if filt == {}:
            print("No filter set")
        else:
            print("Chain\tAction")
            for i in filt:
                print(filt[i]['chain']+"\t"+filt[i]['action'])
        return filt

    def addFilter(self,chain):
        """
        Method will add filter
        :param chain: connected-in, dynamic-in
        :return:
        """
        filt = self.client.talk(['/routing/filter/add','=chain='+chain])
        return filt

    def removeFilter(self,number):
        """
        Method wil lremove filter
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/remove', '=numbers=' + number] )
        return filt

    def disableFilter(self,number):
        """
        Method will disable filter
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/disable', '=numbers=' + number] )
        return filt

    def enableFilter(self,number):
        """
        Method will enable filter
        :param number:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/enable', '=numbers=' + number] )
        return filt

    def commentFilter(self,number,comment):
        """
        Method will add comment for filter
        :param number:
        :param comment:
        :return:
        """
        filt = self.client.talk( ['/routing/filter/comment', '=numbers=' + number,'=comment='+comment] )
        return filt