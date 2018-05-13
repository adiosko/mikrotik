from tikapy import TikapyClient
from tikapy import TikapySslClient

class interfacePppClientSetSetGeneral:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)


    def setName(self,name,newName):
        """
        Method will set name
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/interface/ppp-client/set','=numbers='+name,'=name='+newName])
        return ppp

    def setPort(self,name,port):
        """
        Method will set port
        :param name:
        :param port:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=port=' + port] )
        return ppp

    def setApn(self,name,apn):
        """
        Method will set acess point name
        :param name:
        :param apn:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=apn=' + apn] )
        return ppp

    def setPin(self,name,pin):
        """
        Method will set pin
        :param name:
        :param pin:
        :return:
        """
        ppp = self.client.talk( ['/interface/ppp-client/set', '=numbers=' + name, '=pin=' + pin] )
        return ppp