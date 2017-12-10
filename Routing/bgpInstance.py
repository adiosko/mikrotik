from tikapy import TikapyClient
from tikapy import TikapySslClient

class BGPInstance:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listInstances(self):
        """
        Method wil list all instances
        :return:
        """
        inst = self.client.talk(['/routing/bgp/instance/print'])
        if inst == {}:
            print("No instance found")
        else:
            print("Name\tAS\tRouter-ID")
            for i in inst:
                print(inst[i]['name']+"\t"+inst[i]['as']+"\t"+inst[i]['router-id'])
        return inst

    def addInstance(self,AS,RtID):
        """
        Method will add new instance based on Autonomous system and router id
        :param AS: as number till 65535
        :param RtID: IP of loopback
        :return:
        """
        inst = self.client.talk(['/routing/bgp/instance/add','=as='+AS,'=router-id='+RtID])
        return inst

    def removeInstance(self,name):
        """
        Method will remove instance based on its name
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/remove', '=numbers='+name] )
        return inst

    def disableInstance(self,name):
        """
        Method will disable instance based on its name
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/disable', '=numbers=' + name] )
        return inst

    def enableInstance(self, name):
        """
        Method will disable instance based on its name
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/enable', '=numbers=' + name] )
        return inst

    def commentInstance(self,name,comment):
        """
        Methodwill comment instance
        :param name:
        :param comment:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/comment', '=numbers=' + name,'=comment='+comment] )
        return inst

    def setInstanceName(self,oldName,newName):
        """
        Method will rename instance
        :param oldName:
        :param newName:
        :return:
        """
        inst = self.client.talk(['/routing/bgp/instance/set','=numbers='+oldName,'=name='+newName])
        return inst

    def setAS(self,name,AS):
        """
        Method will set AS number
        :param name:
        :param AS:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=as=' + AS] )
        return inst

    def setRouterID(self,name,RID):
        """
        MEthod will set rid
        :param name:
        :param RID:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=router-id=' + RID] )
        return inst

    def setRedistributeConnected(self,name):
        """
        MEthod will redistribute connected networks
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=redistribute-connected=yes'] )
        return inst

    def setRedistributeStatic(self, name):
        """
        MEthod will redistribute connected networks
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=redistribute-static=yes'] )
        return inst

    def setRedistributeRIP(self, name):
        """
        MEthod will redistribute connected networks
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=redistribute-rip=yes'] )
        return inst

    def setRedistributeOSPF(self, name):
        """
        MEthod will redistribute connected networks
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=redistribute-ospf=yes'] )
        return inst

    def setRedistributeBGP(self, name):
        """
        MEthod will redistribute connected networks
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=redistribute-other-bgp=yes'] )
        return inst

    def setOuterFiler(self,name,filter):
        """
        Method will set out filer
        :param name:
        :param filter: connected-in,dynamic-in,rip-in,rip-out
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=out-filter='+filter] )
        return inst

    def setConfederation(self,name,confederation="0"):
        """
        MEthod will setup confederation
        :param name:
        :param confederation: def 0
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=confederation=' +confederation])
        return inst

    def setConfederationPeer(self,name,peer="0"):
        """
        Method will set peer
        :param name:
        :param peer:  def 0
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=confederation-peers='+peer] )
        return inst

    def setClusterID(self,name,CID):
        """
        Method will set clusted ID
        :param name:
        :param CID:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=cluster-id=' + CID] )
        return inst

    def setRoutingTable(self,name,rtrTable="main"):
        """
        Method will set routing table mainly it is main
        :param name:
        :param rtrTable:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=routing-table=' + rtrTable] )
        return inst

    def setClientToClientReflection(self,name):
        """
        Method will set client to client reflection
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=client-to-client-reflection=yes'] )
        return inst

    def setIgnoreAsPathLength(self,name):
        """
        Method will ignore as path
        :param name:
        :return:
        """
        inst = self.client.talk( ['/routing/bgp/instance/set', '=numbers=' + name, '=ignore-as-path-len=yes'] )
        return inst


