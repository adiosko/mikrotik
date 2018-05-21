from tikapy import TikapyClient
from tikapy import TikapySslClient

class bgpAgregates:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listAgregation(self):
        """
        Method will list agregation
        :return:
        """
        agr = self.client.talk(['/routing/bgp/aggregate/print'])
        if agr == {}:
            print("nothing set")
        else:
            print("Prefix\tSummary only\tinherit attributes\tinclude igp")
            for i in agr:
                print(agr[i]['prefix']+"\t"+agr[i]['summary-only']+"\t"+agr[i]['inherit-attributes']+"\t"+agr[i]
                ['include-igp'])
        return agr

    def addAggregation(self,prefix,instance):
        """
        Method will add Aggregation
        :param prefix: IP
        :param instance: profile
        :return:
        """
        agr = self.client.talk(['/routing/bgp/aggregate/add','=prefix='+prefix,'=instance='+instance])
        return agr

    def removeAggregation(self,number):
        """
        Methodwill remove aggregation
        :param number:
        :return:
        """
        agr = self.client.talk(['/routing/bgp/aggregate/remove','=numbers='+number])
        return agr

    def disableAggregation(self,number):
        """
        Method will disable aggregation
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/disable', '=numbers=' + number] )
        return agr

    def enableAggregation(self,number):
        """
        Method will enable aggregation
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/enable', '=numbers=' + number] )
        return agr

    def setInstance(self,number,instance):
        """
        Method will set aggregaton
        :param number:
        :param instance:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number,'=instance='+instance] )
        return agr

    def setPrefix(self,number,prefix):
        """
        Method will set new prefix
        :param number:
        :param prefix:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=prefix=' + prefix] )
        return agr

    def setSummaryOnly(self,number):
        """
        Method will set sumamry only
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=summary-only=yes'] )
        return agr

    def unsetSummaryOnly(self, number):
        """
        Method will set sumamry only
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=summary-only=no'] )
        return agr

    def setInheritAttributes(self,number):
        """
        Method will enable inherit attributes
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=inherit-attributes=yes'] )
        return agr

    def unsetInheritAttributes(self, number):
        """
        Method will enable inherit attributes
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=inherit-attributes=no'] )
        return agr

    def setIncludeIGP(self,number):
        """
        Method will include IGP
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=include-igp=yes'] )
        return agr

    def unsetIncludeIGP(self, number):
        """
        Method will include IGP
        :param number:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=include-igp=no'] )
        return agr

    def setAttributeFilter(self,number,atribute):
        """
        Method will set attribute filter
        :param number:
        :param atribute: dyamic-in, conencted-in, rip-in, rip-out
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=attribute-filter='+atribute] )
        return agr

    def setSupressFilter(self,number,filter):
        """
        Method will set supress filter
        :param number:
        :param filter:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=suppress-filter=' + filter] )
        return agr

    def setAdvertiseFilter(self,number,filter):
        """
        Method will set advertisment filter
        :param number:
        :param filter:
        :return:
        """
        agr = self.client.talk( ['/routing/bgp/aggregate/set', '=numbers=' + number, '=advertise-filter=' + filter] )
        return agr