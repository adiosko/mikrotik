from tikapy import TikapyClient
from tikapy import TikapySslClient

class QueueInterfaces:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listQueueInterfaces(self):
        """
        Method will list all queue interfaces
        :return:
        """
        queue = self.client.talk(['/queue/interface/print'])
        if queue == {}:
            print("No queue interface found")
        else:
            print("interface\tQueue type\t Active Queue type")
            for i in queue:
                print(queue[i]['interface']+"\t"+queue[i]['queue']+"\t"+queue[i]['active-queue'])
        return queue

    def setQueueInterface(self,interface,type):
        """
        Method will set queue interface type of queue
        :param interface:
        :param type: default,default-small,ethernet-default,hotspot-default, multi-queue-ethernet-default,
        only-hardware-queue,pcq-download-default , pcq-upload-default, synchronous-default, wireless-default
        :return:
        """
        queue = self.client.talk(['/queue/interface/set','=numbers='+interface,'=queue='+type])
        return queue