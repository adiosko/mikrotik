from tikapy import TikapyClient
from tikapy import TikapySslClient

class profileGeneral:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setName(self,name,newName):
        """
        Method will set new name
        :param name:
        :param newName:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=name='+newName])
        return ppp

    def setLocalAddress(self,name,locaddr):
        """
        Method will set local address
        :param name:
        :param locaddr:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=local-address=' + locaddr])
        return ppp

    def setRemoteAddress(self,name,addr):
        """
        Method will set remote address
        :param name:
        :param addr:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=remote-address=' + addr])
        return ppp

    def setBridge(self,name,bridge):
        """
        Method will set bridge
        :param name:
        :param bridge:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=bridge=' + bridge])
        return ppp

    def setBridgePortPriority(self,name,priority="80"):
        """
        Method will set bridge port priority
        :param name:
        :param priority:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=bridge-port-priority=' + priority])
        return ppp

    def setBridgeParhCOst(self,name,cost="10"):
        """
        Method will set bridge path cost
        :param name:
        :param cost:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=bridge-path-cost=' + cost])
        return ppp

    def setBridgeHorizon(self,name,horizon="0"):
        """
        Method will set bridge horizon
        :param name:
        :param horizon:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=bridge-horizon=' + horizon])
        return ppp

    def setIncominFilter(self,name,filter):
        """
        Method will set incoming filter
        :param name:
        :param filter:input,forward,output
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=incoming-filter=' + filter])
        return ppp

    def setOutgoingFilter(self,name,filter):
        """
        Method will set outgoing filter
        :param name:
        :param filter: input,forward,output
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=outgoing-filter=' + newName])
        return ppp

    def setAddressList(self,name,addr):
        """
        Method will set address list
        :param name:
        :param addr: address list
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=address-list=' + addr])
        return ppp

    def setInterfaceList(self,name,ifacelist):
        """
        Method will set interface list
        :param name:
        :param ifacelist:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=interface-list=' + ifacelist])
        return ppp

    def setDnsServer(self,name,dns):
        """
        Method will set dns servers
        :param name:
        :param dns:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=dns-server=' + dns])
        return ppp

    def setWinsServer(self,name,wins):
        """
        Method will set wins server
        :param name:
        :param wins:
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=wins-server=' + wins])
        return ppp

    def changeTcpMss(self,name,change="yes"):
        """
        Method will set change tcp mss
        :param name:
        :param change: yes, no, default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=change-tcp-mss=' + change])
        return ppp

    def useUpnp(self,name,upnp="default"):
        """
        Method will set usage of upnp
        :param name:
        :param upnp: yes,no,default
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=use-upnp='+upnp])
        return ppp