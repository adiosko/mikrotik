from tikapy import TikapyClient
from tikapy import TikapySslClient

class Services:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listServices(self):
        """
        Method will list all dude services on mikrotik
        :return: list
        """
        serv = self.client.talk(['/dude/service/print'])
        if serv == {}:
            print("No service enabled")
        else:
            print("Name")
            for i in serv:
                print(serv[i]['name'])
        return serv

    def addService(self,name):
        """
        Method will add dude service
        :param name: name of service
        :return: list
        """
        serv = self.client.talk(['/dude/service/add','=name='+name])
        return serv

    def setService(self,number,name):
        """
        Method will set ecisting service
        :param number: number of order of service
        :param name: new name of service
        :return: list
        """
        serv = self.client.talk(['/dude/service/set','=numbers='+number,'=name='+name])
        return name

    def removeService(self,name):
        """
        Method will remove service by order #
        :param name: order # of service
        :return: list
        """
        serv = self.client.talk(['/dude/service/remove','=numbers='+name])
        return name

    def commentService(self,name,comment):
        """
        Method will comment service
        :param name: number order of service
        :param comment: comment to use
        :return:  list
        """
        serv = self.client.talk(['/dude/service/comment','=numbers='+name,'=comment='+comment])
        return serv