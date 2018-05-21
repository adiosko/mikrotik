from tikapy import TikapyClient
from tikapy import TikapySslClient

class PimMRib:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRibs(self):
        """
        Method will list rps
        :return:
        """
        pim = self.client.talk(['/routing/pim/mrib/print'])
        if pim == {}:
            print("no rp found")
        else:
            print("Destination\tGateway\tInterface\tmetric\tDynamicState")
            for i in pim:
                #print(pim[i])
                print(pim[i]['destination']+"\t"+pim[i]['gateway']+"\t"+pim[i]['metric'])
        return pim

    def addRibs(self,gateway):
        """
        Method will add pim bsr candidate based on interface
        :param gateway: IP of gw
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/add','=gateway='+gateway] )
        return pim

    def removeMrib(self,number):
        """
        Method will remove rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/remove', '=numbers=' + number] )
        return pim

    def enableMrib(self,number):
        """
        Method will enable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/enable', '=numbers=' + number] )
        return pim

    def disableMrib(self,number):
        """
        Method will disable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/disable', '=numbers=' + number] )
        return pim

    def commentCandidate(self,number,comment):
        """
        Method will comment rp
        :param number:
        :param comment:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/comment', '=numbers=' + number,'=comment='+comment] )
        return pim

    def setDestination(self,number,destination="0.0.0.0/0"):
        """
        Method will set destination
        :param number:
        :param destination: must be subnet not IP
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/set', '=numbers=' + number, '=destination=' + destination] )
        return pim

    def setGateway(self,number,gw):
        """
        Method will set gw
        :param number:
        :param gw: IP of gw not subnet
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/set', '=numbers=' + number, '=gateway=' + gw] )
        return pim

    def setMetric(self,number,metric="1"):
        """
        Method will set emtric for rule
        :param number:
        :param metric:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/mrib/set', '=numbers=' + number, '=metric=' + metric] )
        return pim
