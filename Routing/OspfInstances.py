from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfInstances:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listInstances(self):
        """
        Method will list ospf instances
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/instance/print'])
        if ospf == {}:
            print("No ospf instance set")
        else:
            print("Name\tRouter ID\tState")
            for i in ospf:
                print(ospf[i]['name']+"\t"+ospf[i]['router-id']+"\t"+ospf[i]['state'])
        return ospf

    def addInstance(self):
        """
        Method will add instance
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/add'] )
        return ospf

    def removeInstance(self,name):
        """
        Method willremove ospf instance
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/remove','=numbers='+name] )
        return ospf

    def disableInstance(self,name):
        """
        Method will disable instance
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/disable','=numbers='+name] )
        return ospf

    def enableInstance(self,name):
        """
        Method will enable instance
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/enable','=numbers='+name] )
        return ospf

    def commentInstance(self,name,comment):
        """
        Method will comment instance
        :param name:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/comment', '=numbers=' + name,'=comment='+comment] )
        return ospf

    def setInstanceName(self,name,newName):
        """
        Method will rename instance
        :param name:
        :param newName:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name,'=name='+newName] )
        return ospf

    def setRId(self,name,RID="0.0.0.0"):
        """
        Method will set router id
        :param name:
        :param RID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=router-id=' + RID] )
        return ospf

    def setRedistributeDefaultRoute(self,name,redist="never"):
        """
        Method will set rid
        :param name:
        :param redist: never,always-as-type-1,always-as-type-2,if-installed-as-type-1,if-installed-as-type-2,never
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=distribute-default=' + redist] )
        return ospf

    def setRedistributeCOnnectedNetworks(self,name,redist="no"):
        """
        Method will redistribute connected networks
        :param name:
        :param redist: no,as-type-1,as-type-2
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=redistribute-connected=' + redist])
        return ospf

    def setRedistributeStatic(self,name,redist="no"):
        """
        Method will redistribute static route
        :param name:
        :param redist: no, as-type-1,as-type-2
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/instance/set', '=numbers=' + name, '=redistribute-static=' + redist] )
        return ospf

    def setRedistributeRip(self,name,redist="no"):
        """
        Method will redistribute rip
        :param name:
        :param redist: no,as-type-1,as-type-2
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=redistribute-rip=' + redist] )
        return ospf

    def setRedistributeBgp(self,name,redist="no"):
        """
        Method will redistribure bgp
        :param name:
        :param redist: no,as-type-1,as-type-2
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=redistribute-bgp=' + redist] )
        return ospf

    def setRedistributeOspf(self,name,redist="no"):
        """
        Method will redistribute other ospf
        :param name:
        :param redist: no, as-type-1,as-type-2
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=redistribute-other-ospf=' + redist] )
        return ospf

    def setInFilter(self,name,filt="ospf-in"):
        """
        Method will set ospf input filter
        :param name:
        :param filt: ospf-in,connected-in,dynamic-in,mme-in,ospf-out
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/instance/set', '=numbers=' + name, '=in-filter=' + filt] )
        return ospf

    def setOutFilter(self,name,filt="ospf-out"):
        """
        Method will set ouput flter
        :param name:
        :param filt: ospf-in,connected-in,dynamic-in,mme-in,ospf-out
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=out-filter=' + filt] )
        return ospf

    def setDefaultMettric(self,name,metric="1"):
        """
        Method will set def metric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-default=' + metric] )
        return ospf

    def setConnectedMetric(self,name,metric="20"):
        """
        Methgod will ste connecte dmetric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-connected=' + metric] )
        return ospf

    def setStaticMetric(self,name,metric="20"):
        """
        Method will set static metric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-static=' + metric] )
        return ospf

    def setRipMetric(self,name,metric="20"):
        """
        Method will set default metric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-rip=' + metric] )
        return ospf

    def setBgpMetric(self,name,metric="0"):
        """
        Method will set bgp metric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-bgp=' + metric] )
        return ospf

    def setOspfMetric(self,name,metric="0"):
        """
        Method will set ospf metric
        :param name:
        :param metric:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=metric-other-ospf=' + metric] )
        return ospf

    def setMplsTeArea(self,name,area="backbone"):
        """
        Method will set mpls area
        :param name:
        :param area: backbone
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=mpls-te-area=' + area] )
        return ospf

    def setMplsTeRputerId(self,name,interface="ether1"):
        """
        Method will set mpls interface for rid
        :param name:
        :param interface:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=mpls-re-router-id=' + interface] )
        return ospf

    def setMplsRoutingTable(self,name,rtable="main"):
        """
        Method will set routing table
        :param name:
        :param rtable:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/instance/set', '=numbers=' + name, '=routing-table=' + rtable] )
        return ospf