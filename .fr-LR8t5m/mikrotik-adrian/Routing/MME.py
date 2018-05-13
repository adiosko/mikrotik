from tikapy import TikapyClient
from tikapy import TikapySslClient

class MME:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listMmeInterface(self):
        """
        Method will list mme interfaces
        :return:
        """
        mme = self.client.talk(['/routing/mme/interface/print'])
        if mme == {}:
            print("No mme iface fset")
        else:
            print("Interface\tPassive\tPrimary\tTx/Rx")
            for i in mme:
                print(mme[i]['interface']+"\t"+mme[i]['passive']+"\t"+mme[i]['primary']+"\t"+mme[i]['messages-tx']+"/"
                      +mme[i]['messages-rx'])
        return mme

    def addInterface(self,interface="all"):
        """
        Method will add mme interface
        :param interface:
        :return:
        """
        mme = self.client.talk(['/routing/mme/interface/add','=interface='+interface])
        return mme

    def removeInterface(self,number):
        """
        Method will remove interface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/remove', '=numbers=' + number] )
        return mme

    def disableInterface(self,number):
        """
        Method will disbale iface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/disable', '=numbers=' + number] )
        return mme

    def enableInterface(self,number):
        """
        Method will enable iface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/enable', '=numbers=' + number] )
        return mme

    def setPassiveInterface(self,number):
        """
        Method will set passive iface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/set', '=numbers=' + number,'=passive=yes'] )
        return mme

    def unsetPassiveInterface(self, number):
        """
        Method will set passive iface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/set', '=numbers=' + number, '=passive=no'] )
        return mme

    def setPrimaryInterface(self,number):
        """
        Method will set primary interface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/set', '=numbers=' + number, '=primary=yes'] )
        return mme

    def unsetPrimaryInterface(self, number):
        """
        Method will set primary interface
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/interface/set', '=numbers=' + number, '=primary=no'] )
        return mme

    def setMmeOriginInterval(self,interval="00:00:05"):
        """
        method will set origin interval
        :param interval:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=origination-interval='+interval] )
        return mme

    def setMmmeTimeout(self,time="00:01:00"):
        """
        Method will set timeout
        :param time:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=timeout=' + time] )
        return mme

    def setBidirectionalTimeout(self,time="00:00:02"):
        """
        Method will set bidirectoional timeout
        :param time:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=bidirectional-timeout=' + time] )
        return mme

    def setTtl(self,ttl="50"):
        """
        method will set default ttl
        :param ttl:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=ttl=' + ttl] )
        return mme

    def setGatewayClass(self,clas="none"):
        """
        Method will set gw class
        :param clas: 1-MBit,2-MBit,3-MBit,5-MBit,6-MBit,56-KBit,64-KBit,128-KBit,256-KBit,512-KBit,>6-MBit
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=gateway-class=' + clas] )
        return mme

    def setGwSelection(self,gw="no-gateway"):
        """
        Method will gw selection
        :param gw:  no-gateway,best-statistic,best-adjusted
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=gateway-selection=' + gw] )
        return mme

    def setGwKeepalive(self,keep="00:01:00"):
        """
        Method will set keeepalive for gw
        :param keep:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=gateway-keepalive=' + keep] )
        return mme

    def setPreferredGw(self,gw="0.0.0.0"):
        """
        Method will set preferred gw
        :param gw:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/set', '=preferred-gateway=' + gw] )
        return mme

    def listNetworks(self):
        """
        Method will list mme networks
        :return:
        """
        mme = self.client.talk( ['/routing/mme/network/print'] )
        if mme =={}:
            print("No network set")
        else:
            print("Network")
            for i in mme:
                print(mme[i]['network'])
        return mme

    def addNetwork(self,net="0.0.0.0/0"):
        """
        Method will add mme net
        :param net:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/network/add','=network='+net] )
        return mme

    def removeNetwork(self,number):
        """
        Method will remove network
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/network/remove', '=numbers=' + number] )
        return mme

    def disableNetwork(self,number):
        """
        Method will disable net
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/network/disable', '=numbers=' + number] )
        return mme

    def enableNetwork(self,number):
        """
        Method will enable net
        :param number:
        :return:
        """
        mme = self.client.talk( ['/routing/mme/network/enable', '=numbers=' + number] )
        return mme

    def listOriginators(self):
        """
        Method will list all originators
        :return:
        """
        mme = self.client.talk( ['/routing/mme/originators/print'] )
        return mme