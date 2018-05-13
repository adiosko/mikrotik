from tikapy import TikapyClient
from tikapy import TikapySslClient

class RpCandidate:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listCandidates(self):
        """
        Method will list rps
        :return:
        """
        pim = self.client.talk(['/routing/pim/rp-candidates/print'])
        if pim == {}:
            print("no rp found")
        else:
            print("group\tinterface\tIs scope zone\tpriority\tholdtime")
            for i in pim:
                #print(pim[i])
                print(pim[i]['group']+"\t"+pim[i]['interface']+"\t"+pim[i]['is-scope-zone']+"\t"+pim[i]['priority']+"\t"+pim[i]['holdtime'])
        return pim

    def addCandidate(self,interface):
        """
        Method will add pim bsr candidate based on interface
        :param interface:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/add','=interface='+interface] )
        return pim

    def removeCandidate(self,number):
        """
        Method will remove rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/remove', '=numbers=' + number] )
        return pim

    def enableCandidate(self,number):
        """
        Method will enable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/enable', '=numbers=' + number] )
        return pim

    def disableCandidate(self,number):
        """
        Method will disable rp
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/disable', '=numbers=' + number] )
        return pim

    def commentCandidate(self,number,comment):
        """
        Method will comment rp
        :param number:
        :param comment:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/comment', '=numbers=' + number,'=comment='+comment] )
        return pim

    def setGroup(self,number,group="224.0.0.0/4"):
        """
        Method will set scope zone
        :param number:
        :param group: multicast subnet
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/set', '=numbers=' + number, '=group=' + group] )
        return pim

    def setInterface(self,number,interface="ether1"):
        """
        Method will set interface ffor scope
        :param number:
        :param interface:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/set', '=numbers=' + number, '=interface=' + interface] )
        return pim

    def enableIpScopeZone(self,number):
        """
        Method will enable scope zone
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/set', '=numbers=' + number, '=disabled=no'] )
        return pim

    def disableIpScopeZone(self,number):
        """
        Method will disable zone
        :param number:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/rp-candidates/set', '=numbers=' + number, '=disabled=yes'] )
        return pim

    def setPriority(self,number,priority="192"):
        """
        Method will set priority for scopezone
        :param number:
        :param priority:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/bsr-candidates/set', '=numbers=' + number, '=priority=' + priority] )
        return pim

    def setHoldtime(self,number,holdtime="00:02:30"):
        """
        Method will set hash length
        :param number:
        :param holdtime:
        :return:
        """
        pim = self.client.talk( ['/routing/pim/bsr-candidates/set', '=numbers=' + number, '=holdtime=' + holdtime] )
        return pim