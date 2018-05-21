from tikapy import TikapyClient
from tikapy import TikapySslClient

class Accounting:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def enableAccounting(self):
        """
        Method will enable accounting
        :return:
        """
        ipv4 = self.client.talk(['/ip/accounting/set','=enabled=yes'])
        return ipv4

    def disableAccounting(self):
        """
        Method will enable accounting
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/set', '=enabled=no'] )
        return ipv4

    def enableLocalTraffic(self):
        """
        Method will enable local traffic
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/set', '=account-local-traffic=yes'] )
        return ipv4

    def disableLocalTraffic(self):
        """
        Method will enable local traffic
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/set', '=account-local-traffic=no'] )
        return ipv4

    def setThreshold(self,threshold="256"):
        """
        Method will set threshold
        :param threshold:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/set', '=threshold='+threshold] )
        return ipv4

    def takeSnapshot(self):
        """
        Method will take machine snapshot
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/snapshot/take'] )
        return ipv4

    def printSnapshot(self):
        """
        Method will print snapshots
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/snapshot/print'] )
        for i in ipv4:
            print(ipv4[i])
        return ipv4

    def printWebAccess(self):
        """
        Method woill print web access settings
        :return:
        """
        ipv4 = self.client.talk(['/ip/accounting/web-access/print'])
        for i in ipv4:
            print(ipv4[i])
        return ipv4


    def setAccessibleViaWeb(self):
        """
        Method will set web access
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/web-access/set','=accessible-via-web=yes'] )
        return ipv4

    def unsetAccessibleViaWeb(self):
        """
        Method will set web access
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/web-access/set', '=accessible-via-web=no'] )
        return ipv4

    def setWebAccessAddress(self,address="0.0.0.0/0"):
        """
        Method will set address of web server
        :param address:
        :return:
        """
        ipv4 = self.client.talk( ['/ip/accounting/web-access/set', '=address='+address] )
        return ipv4
