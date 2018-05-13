from tikapy import TikapyClient
from tikapy import TikapySslClient

class RouteRules:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listRules(self):
        """
        Method will lis trules
        :return:
        """
        route = self.client.talk(['/ip/route/rule/print'])
        print("Src address\tDst address\tRoute mark\tInterface\tAction\tTable")
        for i in route:
            print(route[i]['src-address']+"\t"+route[i]['dst-address']+"\t"+route[i]['routing-mark']+"\t"+route[i]['interface']+"\t"+route[i]['action']+"\t"+route[i]['table'])
        return route

    def removeRule(self,number):
        """
        Method will remove rule
        :param number:
        :return:
        """
        rule = self.client.talk(['/ip/route/rule/remove','=numbers='+number])
        return rule

    def enableRule(self, number):
        """
        Method will enable rule
        :param number:
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/enable', '=numbers=' + number] )
        return rule

    def disableRule(self, number):
        """
        Method will remove rule
        :param number:
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/disable', '=numbers=' + number] )
        return rule

    def commentRule(self,number,comment):
        """
        Method will comment rule
        :param number:
        :param comment:
        :return:
        """
        rule = self.client.talk(['/ip/route/rule/comment','=numbers='+number,'=comment='+comment])
        return rule

    def setSrcAddress(self,number,src):
        """
        Method will set src addr
        :param number:
        :param src:
        :return:
        """
        rule = self.client.talk(['/ip/route/rule/set','=number='+number,'=src-address='+src])
        return rule

    def setDstAddress(self, number, dst):
        """
        Method will set dst addr
        :param number:
        :param dst:
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/set', '=number=' + number, '=dst-address=' + dst] )
        return rule

    def setRoutingMark(self, number, mark="main"):
        """
        Method will set routing mark
        :param number:
        :param mark: main or custom name
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/set', '=number=' + number, '=routing-mark=' + mark] )
        return rule

    def setInterface(self, number, iface):
        """
        Method will set interface
        :param number:
        :param iface:
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/set', '=number=' + number, '=interface=' + iface] )
        return rule

    def setAction(self,number,action="lookup-only-in-table"):
        """
        Method will set action
        :param number:
        :param action: drop, lookup, lookup-only-in-table,unreachable
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/set', '=number=' + number, '=action=' + action] )
        return rule

    def setTable(self,number,table="main"):
        """
        Method will set rule table
        :param number:
        :param table: main or custom
        :return:
        """
        rule = self.client.talk( ['/ip/route/rule/set', '=number=' + number, '=table=' + table] )
        return rule
