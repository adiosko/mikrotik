from tikapy import TikapyClient
from tikapy import TikapySslClient

class profileQueue:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setInsertQueueBefore(self,name,queue):
        """
        Method will set queue
        :param name:
        :param queue: bottom,fist
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=insert-queue-before='+queue])
        return ppp

    def setParentQueue(self,name,queue="none"):
        """
        Method will set queue parent
        :param name:
        :param queue: none or custom queue
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set', '=numbers=' + name, '=parent-queue=' + queue])
        return ppp

    def setQueueType(self,name,queue="default"):
        """
        method will set queue type
        :param name:
        :param queue: default,defauklt-small,ethernet-default,hotspot-dedault,multi-queue-ethernet-default,only-hardware-queue
        ,pcq-downlaod-default,pcq-upload-default,synchronous-default,
        :return:
        """
        ppp = self.client.talk(['/ppp/profile/set','=numbers='+name,'=queue-type='+queue])
        return ppp