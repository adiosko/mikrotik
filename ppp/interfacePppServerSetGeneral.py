from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppServerSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setName(self,name,newName):
        """
        Method will rename iface
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-server/set','=numbers='+name,'=name='+newName])
        return ppp

    def setMaxMtu(self,name,mtu="1500"):
        """
        Method will set max mtu
        :param name:
        :param mtu:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=max-mtu=' + mtu] )
        return ppp

    def setMaxMru(self,name,mru="1500"):
        """
        Method will set max mru
        :param name:
        :param mru:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=max-mru=' + mru] )
        return ppp

    def setMrru(self,name,mrru="1500"):
        """
        Method will set mrru
        :param name:
        :param mrru:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=mrru=' + mrru] )
        return ppp

    def setPort(self,name,port):
        """

        :param name:
        :param port:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=port=' + port] )
        return ppp

    def setDataChannel(self,name,channel="0"):
        """
        Method will set channel
        :param name:
        :param channel:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=data-channel=' + channel] )
        return ppp

    def  setModemInit(self,name,modem):
        """

        :param name:
        :param modem:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=modem-init=' + modem] )
        return ppp

    def enableNullModem(self,name):
        """
        Method will enable null modem
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=null-modem=yes'] )
        return ppp

    def disableNullModem(self,name):
        """
        Method will disable null modem
        :param name:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-server/set', '=numbers=' + name, '=null-modem=no'] )
        return ppp