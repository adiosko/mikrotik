from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class UsersGroupSet:
    def __init__(self,address,username,password):
        self.client = TikapyClient(address,8728)
        self.client.login( username,password )

    def setName(self,name,newName):
        """

        :param name:
        :param newName:
        :return:
        """
        user =self.client.talk(['/user/group/set','=numbers='+name,'=name='+newName])
        return user

    def setPolicies(self,name,policy="api,ftp,password,read,romon,sniff,telnet,tikapp,winbox,dude,local,policy,reboot,sensitive,ssh,test,web,write"):
        """

        :param name:
        :param policy: api,ftp,password,read,romon,sniff,telnet,tikapp,winbox,dude,local,policy,reboot,sensitive,ssh,test,web,write, !
        :return:
        """
        user = self.client.talk(['/user/group/set','=numbers='+name,'=policy='+policy])
        return user

    def setSkin(self,name,skin="default"):
        """

        :param name:
        :param skin: default
        :return:
        """
        user = self.client.talk(['/user/group/set','=numbers='+name,'=skin='+skin])
        return user