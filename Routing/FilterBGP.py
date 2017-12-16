from tikapy import TikapyClient
from tikapy import TikapySslClient

class FilterBGP:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def setASPath(self,number,AS):
        """
        Method will set AS path value
        :param AS:
        :return:
        """
        bgp = self.client.talk(['/routing/filter/set','=numbers='+number,'=bgp-as-path='+AS])
        return bgp

    def setNegativeASPath(self, number, AS):
        """
        Method will set AS path negate value
        :param AS:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path=!' + AS] )
        return bgp

    def setAsPathLength(self,number,length="0-4294967295"):
        """
        Method will set as path length
        :param number:
        :param length:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path-length=' +length] )
        return bgp

    def setNegativeAsPathLength(self,number,length):
        """
        Method will negate as path length
        :param number:
        :param length:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-as-path-length=!' + length] )
        return bgp

    def setBgpWeight(self,number,weight="2147483648-2147483647"):
        """
        Method will set wight of bgp
        :param number:
        :param weight:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-weight=' + weight] )
        return bgp

    def setNegativeBgpWeight(self,number,wright):
        """
        Method will set negative bgp weight
        :param number:
        :param wright:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-weight=!' + wright] )
        return bgp

    def setBgpLocalPref(self,number,lpref="0-4294967295"):
        """
        Method will set local pref
        :param number:
        :param lpref:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-local-pref=' + lpref] )
        return bgp

    def setNegativeLocalPref(self,number,lpref="0-4294967295" ):
        """
        Method will negate lpref
        :param number:
        :param lpref:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-local-pref=!' + lpref] )
        return bgp

    def setMED(self,number,MED="0-4294967295"):
        """
        Method will set MED value of bgp
        :param number:
        :param MED:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-med=' + MED] )
        return bgp

    def setNegativeMED(self, number, MED="0-4294967295"):
        """
        Method will set MED value of bgp
        :param number:
        :param MED:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-med=!' + MED] )
        return bgp

    def setAtomicAggregatyion(self,number,aggregation="present"):
        """
        Method will set aggregation
        :param number:
        :param aggregation: present,absent
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-atomic-aggregate='+aggregation] )
        return bgp

    def setIGPOrigin(self,number):
        """
        Method will set iGP orogin
        :param number:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-origin=igp'] )
        return bgp

    def setEGPOrigin(self, number):
        """
        Method will set iGP orogin
        :param number:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-origin=egp'] )
        return bgp

    def setincompleteOrigin(self, number):
        """
        Method will set iGP orogin
        :param number:
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=bgp-origin=incomplete'] )
        return bgp

    def setLocalOriginatedBgp(self,number,originate="no"):
        """
        Method will set originate
        :param number:
        :param originate: no/yes
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=locally-originated-bgp='+originate] )
        return bgp

    def setBgpCommunities(self,number,community="0:0"):
        """
        Method will set community
        :param number:
        :param community:local-as,no-advertise,no-export
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-bgp-communities='+community] )
        return bgp

    def setInvertedBgpCommunities(self, number, community="0:0"):
        """
        Method will set community
        :param number:
        :param community:local-as,no-advertise,no-export
        :return:
        """
        bgp = self.client.talk( ['/routing/filter/set', '=numbers=' + number, '=append-bgp-communities=!' + community] )
        return bgp

