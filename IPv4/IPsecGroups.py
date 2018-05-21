from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecGroups:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listGroups(self):
        """

        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/group/print'])
        print("Name")
        for i in ipsec:
            print(ipsec[i]['name'])
        return ipsec

    def addGroup(self,name):
        """
        Method will add group
        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/group/add','=name='+name])
        return ipsec

    def removeGroup(self,name):
        """
        Method will remove group
        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/group/remove','=numbers='+name])
        return ipsec

    def setName(self,name,newName):
        """
        Method will rename group
        :param name:
        :param newName:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/policy/group/set','=numbers='+name,'=name='+newName])
        return ipsec