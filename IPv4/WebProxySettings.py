from tikapy import TikapyClient
from tikapy import TikapySslClient

class WebProxySettings:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable proxy
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/set','=enabled=yes'])
        return proxy

    def disable(self):
        """
        Method will disable proxy
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=enabled=no'] )
        return proxy

    def setSrcAddress(self,address="::"):
        """
        Method will set src proxy address
        :param address:
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/set','=src-address='+address])
        return proxy

    def setProxyPort(self,port="8080"):
        """
        Method will set proxy port
        :param port:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=port=' + port] )
        return proxy

    def setAnonymous(self):
        """
        Method set proxy anonymous
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=anonymous=yes'] )
        return proxy

    def unsetAnonymous(self):
        """
        Method set proxy anonymous
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=anonymous=no'] )
        return proxy

    def setParentProxy(self,proxy):
        """
        Method will setparent proxy of proxy
        :param proxy:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=parent-proxy='+proxy] )
        return proxy

    def setParentProxyPort(self,port):
        """
        Method will set parent proxy port
        :param port:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=parent-proxy-port='+port] )
        return proxy

    def setCacheAdministrator(self,cache="webmaster"):
        """
        Method will set cache user for admin
        :param cache:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=cache-administrator='+cache] )
        return proxy

    def setMaxCacheSize(self,cache="unlimited"):
        """
        Method will set cache size
        :param cache:  none, unlimited
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=max-cache-size='+cache] )
        return proxy

    def setMaxCacheObjectSize(self,cache="2048"):
        """
        Method will se cacheobject size on kiB
        :param cache: in KiB
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=max-cache-object-size='+cache] )
        return proxy

    def cacheToDisk(self):
        """
        Method will cache data to disk
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=cache-on-disk=yes'] )
        return proxy

    def notCacheToDisk(self):
        """
        Method will cache data to disk
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=cache-on-disk=no'] )
        return proxy

    def setMAxClientCOnnections(self,maxim="600"):
        """
        Method will set max client connections
        :param maxim:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=max-client-connections=' + maxim] )
        return proxy

    def setMaxServerCOnnections(self,maxim="600"):
        """
        Method will set max server connections
        :param maxim:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=max-server-connections=' + maxim] )
        return proxy

    def setMaxFreshTime(self,time="3d 00:00:00"):
        """
        Method will set max fresh time
        :param time:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=max-fresh-time=' + time] )
        return proxy

    def serializeConnections(self):
        """
        Method will senialize connections
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=serialize-connections=yes'] )
        return proxy

    def unserializeConnections(self):
        """
        Method will senialize connections
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=serialize-connections=no'] )
        return proxy

    def alwaysFromCache(self):
        """
        Method will buffer fromc ache every time
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=always-from-cache=yes'] )
        return proxy

    def notAlwaysFromCache(self):
        """
        Method will buffer fromc ache every time
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=always-from-cache=no'] )
        return proxy

    def cacheDscp(self,dcp="4"):
        """
        Method will cache dscp hits
        :param dcp:
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=cache-hit-dscp='+dcp] )
        return proxy

    def setCachePAth(self,path="web-proxy"):
        """
        Method will se tcache path
        :param path: web-proxy, file path
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/set', '=cache-path=' + path] )
        return proxy

    def clearCache(self):
        """
        Method will clear cache
        :return:
        """
        proxy = self.client.talk(['/ip/proxy/clear-cache'])
        return proxy

    def resetHtml(self):
        """
        Method will reset html
        :return:
        """
        proxy = self.client.talk( ['/ip/proxy/reset-html'] )
        return proxy