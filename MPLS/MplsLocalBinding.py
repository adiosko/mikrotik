from tikapy import TikapyClient
from tikapy import TikapySslClient

class MplsLocalBinding:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listBinding(self):
        """
        Method will list all bindings
        :return:
        """
        mpls = self.client.talk(['/mpls/local-bindings/print'])
        if mpls == {}:
            print("table empty")
        else:
            print("Dst address\tLabel")
            for i in mpls:
                print(mpls[i]['dst-address']+"\t"+mpls[i]['label'])
        return mpls

    def addBinding(self,label):
        """
        Method will add local binding, just dynamic
        :return:
        """
        mpls = self.client.talk(['/mpls/local-bindings/add'])
        return mpls

    def removeBinding(self,number):
        """
        Method will remove binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/remove','=numbers='+number] )
        return mpls

    def enableBinding(self,number):
        """
        Method will enable binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/enable','=numbers='+number] )
        return mpls

    def disableBinding(self,number):
        """
        Method will disable binding
        :param number:
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/disable','=numbers='+number] )
        return mpls

    def commentBinding(self,number,comment):
        """
        Method will comment binding
        :param number:
        :param comment:
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/comment','=numbers='+number,'=comment='+comment] )
        return mpls

    def  setDstAddress(self,number,address="0.0.0.0/0"):
        """
        Method will set dst address
        :param number:
        :param address: address/prefix
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/set','=numbers='+number,'=dst-address='+address] )
        return mpls

    def setLabel(self,number,label="expl-null"):
        """
        Method will set label(dynamic records)
        :param number:
        :param label: alert,expl-null,expl-null6,impl-null,one
        :return:
        """
        mpls = self.client.talk( ['/mpls/local-bindings/set', '=numbers=' + number, '=label=' + label] )
        return mpls