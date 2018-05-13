from tikapy import TikapyClient
from tikapy import TikapySslClient

class PrefixList:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listPrefixLists(self):
        """
        Method will list all prefix lists
        :return:
        """
        prefix = self.client.talk(['/routing/prefix-lists/print'])
        if prefix == {}:
            print("No prefix list set")
        else:
            print("Chain\tPrefix\tAction")
            for i in prefix:
                print(prefix[i]['chain']+"\t"+prefix[i]['prefix']+"\t"+prefix[i]['action'])
        return prefix

    def addPrefixLIst(self, chain):
        """
        Method will add pim based on address/prefix
        :param chain: custom rule chain name
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/add', '=chain=' + chain] )
        return prefix

    def removePrefixLIst(self, number):
        """
        Method will remove rp
        :param number:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/remove', '=numbers=' + number] )
        return prefix

    def enablePrefixList(self, number):
        """
        Method will enable rp
        :param number:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/enable', '=numbers=' + number] )
        return prefix

    def disablePrefixLIst(self, number):
        """
        Method will disable rp
        :param number:
        :return:
        """
        prefix= self.client.talk( ['/routing/prefix-lists/disable', '=numbers=' + number] )
        return prefix

    def commentPrefixList(self, number, comment):
        """
        Method will comment rp
        :param number:
        :param comment:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/comment', '=numbers=' + number, '=comment=' + comment] )
        return prefix

    def setChain(self,number,chain):
        """
        Method will set chain
        :param number:
        :param chain:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=chain=' + chain] )
        return prefix

    def setPrefix(self,number,prefix="0.0.0.0/0"):
        """
        Method will set prefix subnet
        :param number:
        :param prefix:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=prefix=' + prefix] )
        return prefix

    def setPrefixLength(self,number,prefix="0-32"):
        """
        Method will set prefix length
        :param number:
        :param prefix: max 32b
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=prefix-length=' + prefix] )
        return prefix

    def setInvertMatch(self,number):
        """
        Method will inver match
        :param number:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=invert-match=yes'] )
        return prefix

    def setNonInvertMatch(self,number):
        """
        Method will uninvert match
        :param number:
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=invert-match=no'] )
        return prefix

    def setAction(self,number,action="accept"):
        """
        Method will set action of rule
        :param number:
        :param action: accept,discard
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=action=' + action] )
        return prefix

    def setMetric(self,number,metric="1"):
        """
        Method will set metric
        :param number:
        :param metric: base on protocol  or distance
        :return:
        """
        prefix = self.client.talk( ['/routing/prefix-lists/set', '=numbers=' + number, '=set-metric=' + metric] )
        return prefix