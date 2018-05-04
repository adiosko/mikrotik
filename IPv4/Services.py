from tikapy import TikapyClient
from tikapy import TikapySslClient

class Services:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listServices(self):
        """
        Method will list services
        :return:
        """
        service = self.client.talk(['/ip/service/print'])
        print("Name\tPort")
        for i in service:
            print(service[i]['name']+"\t"+service[i]['port'])
        return service

    def enableService(self,name):
        """
        Method will enable service
        :param name:
        :return:
        """
        service = self.client.talk(['/ip/service/enable','=numbers='+name])
        return service

    def disableService(self, name):
        """
        Method will disable service
        :param name:
        :return:
        """
        service = self.client.talk( ['/ip/service/disable', '=numbers=' + name] )
        return service

    def setPort(self,name,port):
        """
        Method will set port
        :param name:
        :param port:
        :return:
        """
        service = self.client.talk(['/ip/service/set','=numbers='+name,'=port='+port])
        return service

    def setAvailableFrom(self,name,address):
        """
        Method will set available from address
        :param name:
        :param address:
        :return:
        """
        service = self.client.talk( ['/ip/service/set', '=numbers=' + name, '=address=' + address] )
        return service

    def setCertificate(self,name,cert):
        """
        Method will se tcertificate for ssl services
        :param name:
        :param cert:
        :return:
        """
        service = self.client.talk( ['/ip/service/set', '=numbers=' + name, '=certificate=' + cert] )
        return service