from tikapy import TikapyClient
from tikapy import TikapySslClient

class Settings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listSettings(self):
        """
        Method will list all dude settings
        :return: list
        """
        sett = self.client.talk(['/dude/print'])
        if sett == {}:
            print("No settings found")
        else:
            for i in sett:
                print(sett)
        return sett

    def enableDude(self,data):
        """
        Method will enable Dude
        :param data: data directory name, default dude
        :return: list
        """
        ena = self.client.talk(['/dude/set','=enabled=yes','=data-directory='+data])
        return ena

    def disableDude(self):
        """
        Method will disable dude
        :return: list
        """
        dis = self.client.talk(['/dude/set','=enabled=no'])
        return dis

