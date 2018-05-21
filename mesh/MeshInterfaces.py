from tikapy import TikapyClient
from tikapy import TikapySslClient

class MeshInterfaces:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listInterfaces(self):
        """
        Method will lis tmesh ifaces
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/print'])
        print("Name\tType\tMtu\tMAC")
        for i in mesh:
            print(mesh[i]['name']+"\t"+mesh[i]['mtu']+"\t"+mesh[i]['mac-address'])
        return mesh

    def addInterface(self,name):
        """
        Method will add mesh interface
        :param name:
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/add','=name='+name])
        return mesh

    def removeInterface(self,name):
        """
        Method will remove emsh interface
        :param name:
        :return:
        """
        mesh = self.client.talk(['/interface/mesh/remove','=numbers='+name])
        return mesh

    def enableInterface(self,name):
        """
        Method will enable interface
        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/enable', '=numbers=' + name] )
        return mesh

    def disableInterface(self,name):
        """
        Method will disable interface
        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/disable', '=numbers=' + name] )
        return mesh

    def commentInterface(self,name,comment):
        """
        Method will comment iface
        :param name:
        :param comment:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/comment', '=numbers=' + name,'=comment='+comment] )
        return mesh

    #general
    def setName(self,name,newName):
        """
        Method will rename interface
        :param name:
        :param newName:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=name=' + newName] )
        return mesh

    def setMtu(self,name,mtu="1500"):
        """
        Method will set mtu
        :param name:
        :param mtu:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=mtu=' + mtu] )
        return mesh

    def setArp(self,name,arp="enabled"):
        """
        Method will set arp
        :param name:
        :param arp: enabled, local-proxy-arp,proxy-arp,reply-only
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=arp=' + arp] )
        return mesh

    def setArpTimeout(self,name,time="00:00:00"):
        """
        Method will set arp timeout
        :param name:
        :param time:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=arp-timeout=' + time] )
        return mesh

    def setAdminMac(self,name,mac):
        """
        Method will ste admin mac address
        :param name:
        :param mac:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=admin-mac=' + mac] )
        return mesh

    #Hwsp
    def setMeshPortal(self,name):
        """
        Method will enable mash portal
        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=mesh-portal=yes'] )
        return mesh

    def setDefaultHopLimit(self,name,limit="32"):
        """
        Method will set hop ;limit
        :param name:
        :param limit:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-default-hoplimit=' + limit] )
        return mesh

    def setPreqWaitingTime(self,name,time="4"):
        """
        Method will set preq waiting time in secs
        :param name:
        :param time:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-preq-waiting-time=' + time] )
        return mesh

    def setPreqRetries(self,name,retr="2"):
        """
        Method will set preq retries
        :param name:
        :param retr:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-preq-retries=' + retr] )
        return mesh

    def setPreqDestinationOnly(self,name):
        """

        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-preq-destination-only=yes'] )
        return mesh

    def setPreqReplyAndForward(self,name):
        """

        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-preq-reply-and-forward=yes'] )
        return mesh

    def setPrepLifetime(self,name,life="00:05:00"):
        """

        :param name:
        :param life:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-prep-lifetime=' + life] )
        return mesh

    def setRannInterval(self,name,interval="00:00:10"):
        """

        :param name:
        :param interval:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-rann-interval=' + interval] )
        return mesh

    def setRannPropagationDelay(self,name,delay="500"):
        """
        Method will set prop delay in ms
        :param name:
        :param delay:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-rann-propagation-delay=' + delay] )
        return mesh

    def setRannLifetime(self,name,life="00:00:22"):
        """
        Method will set rann lifetime
        :param name:
        :param life:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=hwmp-rann-lifetime=' + life] )
        return mesh

    def reoptimizePaths(self,name):
        """
        Method will reoptimize paths
        :param name:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/set', '=numbers=' + name, '=reoptimize-paths=yes'] )
        return mesh

    def MeshTraceroute(self,iface,address,hoplimit="255",duration="10s"):
        """
        Method will trace mesh iface
        :param iface:
        :param address: mac address to ping
        :param hoplimit:
        :param: duration:
        :return:
        """
        mesh = self.client.talk( ['/interface/mesh/traceroute', '=mesh=' + iface, '=address=' + address,'=hop-limit='+hoplimit,'=duration='+duration] )
        return mesh
