from tikapy import TikapyClient
from tikapy import TikapySslClient

class QueueTree:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def  listQueueTrees(self):
        """
        Method will list all queue trees
        :return:
        """
        queue = self.client.talk(['/queue/tree/print'])
        if queue == {}:
            print("No queue tree set")
        else:
            print( "Name\tParent\tPacket mark\tlimitat\tmax limit\tavg rate\tqueue bytes\tbytes\tpackets" )
            for i in queue:
                #print(queue)
                print(queue[i]['name']+"\t"+queue[i]['parent']+"\t"+queue[i]['packet-mark']
                +"\t"+queue[i]['limit-at']+"\t"+queue[i]['max-limit']+"\t"+queue[i]['rate']+"\t"+queue[i]
                ['queued-bytes']+"\t"+queue[i]['bytes']+"\t"+queue[i]['queued-packets'])
        return queue

    def addQueueTree(self,parent):
        """
        Method will add queue tree
        :param parent: intercae, queue name, global
        :return:
        """
        queue = self.client.talk(['/queue/tree/add','=parent='+parent])
        return queue

    def removeQueueTree(self,name):
        """
        Method will remove queue tree
        :param name: name of tree to remove
        :return:
        """
        queue = self.client.talk(['/queue/tree/remove','=numbers='+name])
        return queue

    def disableQueueTree(self,name):
        """
        Method will disable queue tree
        :param name: name of tree to disable
        :return:
        """
        queue = self.client.talk( ['/queue/tree/disable', '=numbers=' + name] )
        return queue

    def enableQueueTree(self,name):
        """
        Method will enable queue tree
        :param name: name of queue tree to enable
        :return:
        """
        queue = self.client.talk( ['/queue/tree/enable', '=numbers=' + name] )
        return queue

    def commentQueueTree(self,name,comment):
        """
        Method will comment queue tree
        :param name:
        :param comment:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/comment', '=numbers=' + name,'=comment='+comment] )
        return queue

    def resetCounters(self, name):
        """
        Method will rest counters for simple queue
        :param name:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/reset-counters', '=numbers=' + name] )
        return queue

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        queue = self.client.talk( ['/queue/tree/reset-counters-all'] )
        return queue

    def setQueueName(self,name,newName):
        """
        Method will rename queue
        :param name:
        :param newName:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set','=numbers='+name,'=name='+newName] )
        return queue

    def setQueueParent(self,name,parent):
        """
        Method will set queue parent
        :param name:
        :param parent: intercae, queue name, global
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=parent=' + parent] )
        return queue

    def setQueuePacketMark(self,name,mark):
        """
        Method will set packet mark
        :param name:
        :param mark: custom mark
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=packet-mark=' + mark] )
        return queue

    def setQueueType(self,name,type="default-small"):
        """
        Method will set queue type
        :param name:
        :param type: default,default-small,ethernet-default,hotspot-default, multi-queue-ethernet-default,
        only-hardware-queue,pcq-download-default , pcq-upload-default, synchronous-default, wireless-default
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=queue=' + type] )
        return queue

    def setQueuePriority(self,name,priority="8"):
        """
        Method will set queue tree priority
        :param name:
        :param priority: 1-8
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=priority=' + priority] )
        return queue

    def setQueueBucketSize(self,name,size="0.100"):
        """
        Method will set bucket size
        :param name:
        :param size:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=bucket-size=' + size] )
        return queue

    def setLimitAt(self,name,limit):
        """
        Method will set limit
        :param name:
        :param limit: less then max
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=limit-at=' + limit] )
        return queue

    def setMaxLimit(self,name,limit):
        """
        Methopd will set max limit, must eb bigger than imit at
        :param name:
        :param limit:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=max-limit=' + limit] )
        return queue

    def setBustTime(self,name,time):
        """
        Method will set burst time
        :param name:
        :param time:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=burst-time=' + time] )
        return queue

    def setBurstThreshold(self,name,threshold):
        """
        Method will set burst threshold
        :param name:
        :param threshold: bigger than limit and bigge than max limit
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=burst-threshold=' + threshold] )
        return queue

    def setBurstLimit(self,name,limit):
        """
        Method will set limit of threshold, must be bigger than threshold
        :param name:
        :param limit:
        :return:
        """
        queue = self.client.talk( ['/queue/tree/set', '=numbers=' + name, '=burst-limit=' + limit] )
        return queue