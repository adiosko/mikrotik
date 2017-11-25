from tikapy import TikapyClient
from tikapy import TikapySslClient

class NTPclient:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listNTPClient(self):
        """
        Method will list NTP client setup
        :return:  list
        """
        ntp = self.client.talk(['/system/ntp/client/print'])
        if ntp == {}:
            print("No ntp client found")
        else:
            for i in ntp:
                print(ntp)
        return ntp

    def setNTPclient(self,enabled,mode,primary,secondary):
        """
        Method will setup ntp client
        :param enabled: yes/no
        :param mode: unicast, multicast, manycast, broadcast
        :param primary: primary IP of NTP
        :param secondary: NTP server IP
        :return: list
        """
        ntp = self.client.talk(['/system/ntp/client/set','=enabled='+enabled,'=mode='+mode,'=primary-ntp='+
                                primary,'=secondary-ntp='+secondary])
        return ntp