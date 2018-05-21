from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfInterface:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)


    def listInterfaces(self):
        """
        Method will list all ospf ifaces
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/interface/print'])
        if ospf == {}:
            print("No ospf iface defined")
        else:
            print("Interface\tCOst\tPriority\tAuthentication\tauth key\tnetwork type\tinstance\tarea\tneighbors\tstate")
            for i in ospf:
                #print(ospf)
                print(ospf[i]['interface']+"\t"+ospf[i]['cost']+"\t"+ospf[i]['priority']+"\t"+ospf[i]['authentication']
                      +"\t"+ospf[i]['authentication-key']+"\t"+ospf[i]['network-type'])
        return ospf

    def addInterface(self,interface="all"):
        """
        Method will add interface
        :param interface:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/add','=interface='+interface] )
        return ospf

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/interface/remove','=numbers='+number])
        return ospf

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/disable', '=numbers=' + number] )
        return ospf

    def enableInterface(self,number):
        """
        Method will enable interface
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/enable', '=numbers=' + number] )
        return ospf


    def commentInterface(self,number,comment):
        """
        Method will comment interface
        :param number:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/comment', '=numbers=' + number,'=comment='+comment] )
        return ospf

    def setInterface(self,number,interface="all"):
        """
        Method will echange interface
        :param number:
        :param interface:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number,'=interface='+interface] )
        return ospf

    def setCost(self,number,cost="10"):
        """
        Method will set ospf cost
        :param number:
        :param cost:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number,'=cost='+cost] )
        return ospf

    def setPriority(self,number,priority="1"):
        """
        Method will set priority
        :param number:
        :param priority:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=priority=' +priority] )
        return ospf

    def setAuthentication(self,number,type="none"):
        """
        Method will set authentication
        :param number:
        :param type: none,simple,MD5
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=authentication=' + type] )
        return ospf

    def setAuthenticationKey(self,number,key):
        """
        Method will set auth key
        :param number:
        :param key:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=authentication-key=' + key] )
        return ospf

    def setAuthenticationKeyId(self,number,ID="1"):
        """
        Method will set auth key id
        :param number:
        :param ID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=authentication-key-id='+ID] )
        return ospf

    def setNetworkType(self,number,type="broadcast"):
        """
        Method will set network type
        :param number:
        :param type: broadcast, default, nbma, point-to-point,ptmp
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=network-type=' + type] )
        return ospf

    def setInstanceId(self,number,ID="0"):
        """
        Method will set instance id
        :param number:
        :param ID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=instance-id=' + ID] )
        return ospf

    def setPassive(self,number):
        """
        Method will set interface passive
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=passive=yes'] )
        return ospf

    def unsetPassive(self, number):
        """
        Method will set interface passive
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=passive=no'] )
        return ospf

    def setBfd(self,number):
        """
        Method will set to use bfd
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=use-bfd=yes'] )
        return ospf

    def unsetBfd(self, number):
        """
        Method will set to use bfd
        :param number:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=use-bfd=no'] )
        return ospf

    def setRetransmitInterval(self,number,interval="5"):
        """
        Method will set retransmit interval
        :param number:
        :param interval:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=retransmit-interval='+interval])
        return ospf

    def setTransmitDelay(self,number,delay="1"):
        """
        Method will set delay
        :param number:
        :param delay:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=transmit-delay='+delay] )
        return ospf

    def setHelloInterval(self,number,interval="10"):
        """
        Method will set hello interval
        :param number:
        :param interval:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=hello-interval='+interval] )
        return ospf

    def setDeadInterval(self,number,interval="40"):
        """
        Method will set dead interval
        :param number:
        :param interval:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/interface/set', '=numbers=' + number, '=dead-interval='+interval] )
        return ospf