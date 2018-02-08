from tikapy import TikapyClient
from tikapy import TikapySslClient

class Packing:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listPacking(self):
        """
        Method will list packing
        :return:
        """
        pack = self.client.talk(['/ip/packing/print'])
        print("Interface\tPacking\tUnpacking\tAgregate size")
        for i in pack:
            print(pack[i]['interface']+"\t"+pack[i]['packing']+"\t"+pack[i]['unpacking']+"\t"+pack[i]['aggregated-size'])
        return pack

    def addPacking(self,interface):
        """
        Method will add packing
        :param interface:
        :return:
        """
        pack = self.client.talk(['/ip/packing/add','=interface='+interface])
        return pack

    def removePacking(self,number):
        """
        Method will remove packing
        :param number:
        :return:
        """
        pack = self.client.talk(['/ip/packing/remove','=numbers='+number])
        return pack

    def enablePacking(self,number):
        """
        Method will enable packing
        :param number:
        :return:
        """
        pack = self.client.talk( ['/ip/packing/enable', '=numbers=' + number] )
        return pack

    def disablePacking(self,number):
        """
        Method will disable packing
        :param number:
        :return:
        """
        pack = self.client.talk( ['/ip/packing/disable', '=numbers=' + number] )
        return pack

    def setInterface(self,number,iface):
        """
        Method will set packing interface
        :param number:
        :param iface:
        :return:
        """
        pack = self.client.talk( ['/ip/packing/set', '=numbers=' + number,'=interface='+iface] )
        return pack

    def setPacking(self,number,pack="simple"):
        """
        Method will set packing
        :param number:
        :param pack: compress-all,compress-headers,none,simple
        :return:
        """
        pack = self.client.talk( ['/ip/packing/set', '=numbers=' + number, '=packing=' + pack] )
        return pack

    def setUnpacking(self,number,pack="simple"):
        """
        Method will unpack packing
        :param number:
        :param pack:compress-all,compress-headers,none,simple
        :return:
        """
        pack = self.client.talk( ['/ip/packing/set', '=numbers=' + number, '=unpacking=' + pack] )
        return pack

    def setAgregateSize(self,number,agreg="1500"):
        """
        Method will set agregatesize
        :param number:
        :param agreg:
        :return:
        """
        pack = self.client.talk( ['/ip/packing/set', '=numbers=' + number, '=aggregated-size=' + agreg] )
        return pack