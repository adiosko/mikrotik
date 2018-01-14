from tikapy import TikapyClient
from tikapy import TikapySslClient

class RipInterfaces:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will list interfaces
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/print'] )
        if rip == {}:
            print("no rip interface set")
        else:
            print("Interface\tReceive\tsend\tauthentication and authentication key\tkey-chain\tpasisve interface\tprefixlist in and out")
            for i in rip:
                #print(rip[i])
                print(rip[i]['interface']+"\t"+rip[i]['receive']+"\t"+rip[i]['send']+"\t"+rip[i]['authentication']+"\t"
                      +rip[i]['authentication-key']+"\t"+rip[i]['key-chain']+"\t"+rip[i]['passive']+"\t"+rip[i]['in-prefix-list']
                      +rip[i]['out-prefix-list'])
        return rip

    def addInterfaces(self):
        """
        Method will add rip iface
        :return:
        """
        rip = self.client.talk(['/routing/rip/interface/add'])
        return rip

    def removeInterface(self,number):
        """
        Method will remove rip interface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/remove','=numbers='+number] )
        return rip

    def enableInterface(self,number):
        """
        Method will enable iface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/enable', '=numbers=' + number] )
        return rip

    def disableInterface(self,number):
        """
        Method will disable interface
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/disable', '=numbers=' + number] )
        return rip

    def setInterface(self,number,interface="all"):
        """
        Method will set rip interface
        :param number:
        :param interface: all or local interface
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number,'=interface='+interface] )
        return rip

    def setReceive(self,number,rcv="v1-2"):
        """
        Method will set receive version
        :param number:
        :param rcv: v1,v1-2,v2
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number,'=receive='+rcv] )
        return rip

    def setSend(self,number,snd="v2"):
        """
        Method will set interface fdor sending the traffic
        :param number:
        :param snd: v1,v1-2,v2
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=send=' + snd] )
        return rip

    def setAuthentication(self,number,authent="none"):
        """
        Method will set rip authentication
        :param number:
        :param authent: none,simple,md5
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=authentication=' + authent] )
        return rip

    def setAuthenticationKey(self,number,key):
        """
        Method will set authentication key
        :param number:
        :param key: key for simple and md5
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=authentication-key=' + key] )
        return rip

    def setKeyChain(self,number,chain):
        """
        Method will set authentication key chain
        :param number:
        :param chain:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=key-chain=' + chain] )
        return rip

    def setPassiveInterface(self,number):
        """
        Method will set iface passive
        :param number:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=passive=yes'] )
        return rip

    def setInPrefixList(self,number,prefix):
        """
        Method will set input prefix list
        :param number:
        :param prefix:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=in-prefix-list=' + prefix] )
        return rip

    def setOutPrefixList(self,number,prefix):
        """
        Method will set prefix output list
        :param number:
        :param prefix:
        :return:
        """
        rip = self.client.talk( ['/routing/rip/interface/set', '=numbers=' + number, '=out-prefix-list=' + prefix] )
        return rip