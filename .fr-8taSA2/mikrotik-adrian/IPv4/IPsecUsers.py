from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecUsers:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listUsers(self):
        """
        Methodwill list users
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/user/print'])
        print("Name\tPassword\tAddress")
        for i in ipsec:
            print(ipsec[i]['name']+"\t"+ipsec[i]['password']+"\t"+ipsec[i]['address'])
        return ipsec

    def addUser(self,name,password):
        """
        Method will add user
        :param name:
        :param password:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/user/add','=name='+name,'=password='+password])
        return ipsec

    def removeUser(self,name):
        """
        Methodwill remove user
        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/user/remove','=numbers='+name])

    def setName(self,name,newNAme):
        """
        Method will rename user
        :param name:
        :param newNAme:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/user/set','=numbers='+name,'=name='+newNAme])
        return ipsec

    def setPassword(self,name,password):
        """
        Method will set password
        :param name:
        :param password:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/user/set', '=numbers=' + name, '=password=' + password] )
        return ipsec

    def setAddress(self,name,address):
        """
        Method will set user address
        :param name:
        :param address:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/user/set', '=numbers=' + name, '=address=' + address] )
        return ipsec