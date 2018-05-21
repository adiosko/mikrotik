from tikapy import TikapyClient
from tikapy import TikapySslClient

class Notifications:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listNotifications(self):
        """
        Method will list all Dude Notifications
        :return: list
        """
        notif = self.client.talk( ['/dude/notification/print'] )
        if notif == {}:
            print( "No object found" )
        else:
            print( "Name" )
            for i in notif:
                print( notif[i]['name'] )
        return notif

    def addNotification(self, name, comment=None):
        """
        Method will add new Notification
        :param name: name of notification
        :param comment: (optional)
        :return: list
        """
        if comment == None:
            notif = self.client.talk( ['/dude/notification/add', '=name=' + name] )
        else:
            notif = self.client.talk( ['/dude/notification/add', '=name=' + name, '=comment=' + comment] )
        return notif

    def setNotification(self, oldName, newName):
        """
        Method will rename notification
        :param oldName: old name of notification
        :param newName: new name
        :return: list
        """
        notif = self.client.talk( ['/dude/notification/set', '=numbers=' + oldName, '=name=' + newName] )
        return notif

    def removeNotification(self, name):
        """
        Method will remove notification from list of notifications
        :param name: name of notification to remove
        :return: list
        """
        notif = self.client.talk( ['/dude/notification/remove', '=numbers=' + name] )
        return notif

