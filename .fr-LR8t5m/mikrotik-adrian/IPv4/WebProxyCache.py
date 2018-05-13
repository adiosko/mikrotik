from tikapy import TikapyClient
from tikapy import TikapySslClient

class WebProxycache:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listcache(self):
        """
        Method will list cachees
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/cache/print'])
        print("Src address\tDst address\tDst port\taction")
        for i in proxy:
            print(proxy[i]['src-address']+"\t"+proxy[i]['dst-address']+"\t"+proxy[i]['dst-port']+"\t"+proxy[i]['action'])
        return proxy

    def addcache(self,dstPort,action="allow"):
        """
        Method will add new cache
        :param dstPort:
        :param action: allow deny
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/cache/add','=dst-port='+dstPort,'=action='+action])
        return proxy

    def removecache(self,number):
        """
        Method will remove cache
        :param number:
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/cache/remove','=numbers='+number])
        return proxy

    def enablecache(self, number):
        """
        Method will remove cache
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/enable', '=numbers=' + number] )
        return proxy

    def disablecache(self, number):
        """
        Method will remove cache
        :param number:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/disable', '=numbers=' + number] )
        return proxy

    def commentcache(self,number,comment):
        """
        Method will comment cache
        :param number:
        :param comment:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/comment', '=numbers=' + number,'=comment='+comment] )
        return proxy

    def setSrcAddress(self,number,address):
        """
        Method will se tsrc address
        :param number:
        :param address: !,src address
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=src-address=' + address] )
        return proxy

    def setDstAddress(self,number,address):
        """
        Method will setdst address
        :param number:
        :param address: !, address
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=dst-address=' + address] )
        return proxy

    def setDstPort(self,number,port):
        """
        Method will set dst port
        :param number:
        :param port:!,port
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=dst-port=' + port] )
        return proxy

    def setLocalPort(self,number,port="1"):
        """
        Method will set local port
        :param number:
        :param port: !,port
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=local-port=' + port] )
        return proxy

    def setDstHost(self,number,host):
        """
        Method will set dst host
        :param number:
        :param host:!,IP
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=dst-host=' + host] )
        return proxy

    def setPath(self,number,path):
        """
        Method will set path
        :param number:
        :param path: !,path = fiepath dirpath
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=path=' + path] )
        return proxy

    def setMethod(self,number,method="CONNECT"):
        """
        Method will set method
        :param number:
        :param method: !, CONNECT, DELETE, GET, HEAD, OPTIONS,POST,PUT,TRACE
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=method=' + method] )
        return proxy

    def setAction(self,number,action="allow"):
        """
        Method will set action
        :param number:
        :param action: allow,deny
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/set', '=numbers=' + number, '=action=' + action] )
        return proxy

    def resetCounters(self,number):
        """
        Method will reset counters
        :param number:
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/cache/reset-counters','=numbers='+number])
        return proxy

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/cache/reset-counters-all'] )
        return proxy