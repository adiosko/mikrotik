from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint


class Services:
    def __init__(self, address):
        self.client = TikapyClient( address, 8728 )
        self.client.login( 'admin', 'admin' )

    def listServices(self):
        """
        Method which will list all services on mikrotik
        :return: list of services
        """
        services = self.client.talk( ['/ip/service/print'] )
        print("Name \t Port \t Disable status")
        for i in services:
            print( services[i]['name']+" "+services[i]['port']+" "+services[i]['disabled'] )
        return services

    def disableService(self,servicename):
        """
        method which will enable service on mikrotik by its service name
        :param servicename:
        :return: list of enabled services
        """
        services = self.client.talk(['/ip/service/set','=numbers='+servicename,'=disabled=yes'])
        return services

    def enableService(self,servicename):
        """
        method which will enable mikrotik service by its service name
        :param servicename: name of the service you would like to enable
        :return: list of services
        """
        services = self.client.talk(['/ip/service/set','=numbers='+servicename,'=disabled=no'])
        return services