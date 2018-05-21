from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsRemoteBinding:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listRemoteBindings(self):
        """
        Method will list all remote bindings
        :return:
        """
        mpls = self.client.talk(['/mpls/remote-bindings/print'])
        if mpls == {}:
            print("No entry found")
        else:
            print("Dst-address\tLabel\tNexthop")
            for i in mpls:
                print(mpls[i]['dst-address']+"\t"+mpls[i]['label']+"\t"+mpls[i]['nexthop'])
        return mpls

    def addBinding(self):
        """
        Method will add entry
        :return:
        """
        mpls = self.client.talk(['/mpls/remote-bindings/add'])
        return mpls

    def removeBinding(self,number):
        """
        Method will remove binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/remove','=numbers='+number] )
        return mpls

    def enableBinding(self,number):
        """
        Method will enable binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/enable', '=numbers=' + number] )
        return mpls

    def disableBinding(self,number):
        """
        Method will disable binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/disable', '=numbers=' + number] )
        return mpls

    def commentBinding(self,number,comment):
        """
        Method will comment binding
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/comment', '=numbers=' + number,'=comment='+comment] )
        return mpls

    def setDstAddtess(self,number,dstAddress="0.0.0.0/0"):
        """
        Method will set dst address
        :param number:
        :param dstAddress:
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/set', '=numbers=' + number, '=dst-address=' + dstAddress] )
        return mpls

    def setLabel(self,number,label="expl-null"):
        """
        Method will set label
        :param number:
        :param label: alert,expl-null,expl-null6,impl-null,16
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/set', '=numbers=' + number, '=label=' + label] )
        return mpls

    def setNextHop(self,number,nexthop):
        """
        Method will set nhop address
        :param number:
        :param nexthop: <IP>
        :return:
        """
        mpls = self.client.talk( ['/mpls/remote-bindings/set', '=numbers=' + number, '=nexthop=' + nexthop] )
        return mpls





