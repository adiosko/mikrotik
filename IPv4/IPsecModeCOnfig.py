from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecModeConfig:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def lisrConfigs(self):
        """
        Method will list cfgs
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/mode-config/print'])
        print("Name\tDNS")
        for i in ipsec:
            print(ipsec[i]['name']+"\t"+ipsec[i]['send-dns'])
        return ipsec

    def addCfg(self,name):
        """
        Method will add cfg
        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/mode-config/add','=name='+name])
        return ipsec

    def removeCfg(self,name):
        """
        Method will remove cfg
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/remove', '=numbers=' + name] )
        return ipsec

    def enableCfg(self,name):
        """
        Method will enable cfg
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/enable', '=numbers=' + name] )
        return ipsec

    def disableCfg(self,name):
        """
        Method will disable cfg
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/disable', '=numbers=' + name] )
        return ipsec

    def setName(self,name,newName):
        """
        Method will set  new name
        :param name:
        :param newName:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/set', '=numbers=' + name,'=name='+newName] )
        return ipsec

    def setAddressPool(self,name,pool):
        """
        Method will set pool
        :param name:
        :param pool: pool created in pool
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/set', '=numbers=' + name, '=address-pool=' + pool] )
        return ipsec

    def setPrefix(self,name,prefix="24"):
        """
        Method will set pool prefix
        :param name:
        :param prefix:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/set', '=numbers=' + name, '=address-prefix-length=' + prefix] )
        return ipsec

    def setSplitInclude(self,name,address="0.0.0.0/0"):
        """
        Method will set split address
        :param name:
        :param address:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/set', '=numbers=' + name, '=split-include=' + address] )
        return ipsec

    def sendDns(self,name):
        """
        Method will send dns
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/mode-config/set', '=numbers=' + name, '=send-dns=yes'] )
        return ipsec
