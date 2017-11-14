import LoginManager
from os import system
import pexpect
from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint

class Users:
    def __init__(self,address):
        self.client = TikapyClient(address,8728)
        self.client.login( 'admin', 'admin' )

    def listUsers(self):
        users = {}
        #client1 = self.client.login('admin','admin')
        users = self.client.talk(['/user/print'])
        print("System users are: ")
        print("User Disabled Group")
        for i in users:
            print(users[i]['name']+" "+users[i]['disabled']+" "+users[i]['group'])
        return users

    def addUser(self,username,password,disabled,group):
        """
        Method which add new user to mikrotik
        :param username: setup username name
        :param password: username password
        :param disabled: setup username disble status (yes or no)
        :param group: setup user group (read, write,full)
        :return:
        """

        users = self.client.talk(['/user/add','=name='+username,'=password='+password,'=disabled='+disabled,'=group='+group])
        return users

    def deleteUser(self,username):
        """
        Method which remove the user
        :param username:
        :return:
        """
        #self.client.login("admin","admin")
        users = self.client.talk(['/user/remove','=numbers='+username])
        return users

    def changeUserPassword(self,username,password):
        """
        Method which edit user settings on mikrotik
        :param username: username setup
        :param password: username new password
        :return: users with changed password
        """
        users = self.client.talk( ['/user/set', '=numbers='+username, '=password='+password])
        return users

    def enableSystemUser(self,username,disabled):
        """
        enable disabled user
        :param username: username you want to change
         :param disabled: disable status change to no by default
        :return: users
        """
        users = self.client.talk(['/user/set','=numbers='+username,"=disabled="+disabled])
        return users

    def disableUser(self,username,disabled):
        """
        method to disable system user
        :param username: username of user you want to disable
        :param disabled: default yes
        :return: users
        """
        users = self.client.talk(['/user/set','=numbers='+username,"=disabled="+disabled])
        return users

    def changeUserGroup(self,username,group):
        """
        method which will change user group
        :param username: user you wanna modify
        :param group: new user group i.e read,write,full
        :return: users
        """
        #self.client.login( 'admin', 'admin' )
        users = self.client.talk(['/user/set', '=numbers='+username, '=group='+group])
        return users




'''
testovaci kod
users = Users.Users("192.168.1.1")
#users.addUser("adrian","adrian","no","full")
#users.addUser("test","test","yes","read")
#users.listUsers()
#users.changeUserPassword("adrian","adrian1")
#users.changeUserGroup("adrian","read")
#print("\n")
#users.listUsers()
#print("\n")
#users.disableUser("adrian","yes")
#users.listUsers()
#users.enableSystemUser("adrian","no")
#users.listUsers()
#print("\n")
#users.deleteUser("adrian")
#users.deleteUser("adrian1")
'''




