from tikapy import TikapyClient
from tikapy import TikapySslClient

class UpnpSetting:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enable(self):
        """
        Method will enable upnp
        :return:
        """
        upnp = self.client.talk(['/ip/upnp/set','=enabled=yes'])
        return upnp

    def disable(self):
        """
        Method will disable upnp
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/set', '=enabled=no'] )
        return upnp

    def allowToDisableExternalInterface(self):
        """
        Method will allow to disable external iface
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/set', '=allow-disable-external-interface=yes'] )
        return upnp

    def disallowToDisableExternalInterface(self):
        """
        Method will allow to disable external iface
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/set', '=allow-disable-external-interface=no'] )
        return upnp

    def showDummyRule(self):
        """
        Method will show dummy rule
        :return:
        """
        upnp = self.client.talk(['/ip/upnp/set','=show-dummy-rule=yes'])
        return upnp

    def unshowDummyRule(self):
        """
        Method will show dummy rule
        :return:
        """
        upnp = self.client.talk( ['/ip/upnp/set', '=show-dummy-rule=no'] )
        return upnp