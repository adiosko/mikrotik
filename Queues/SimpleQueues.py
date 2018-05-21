from tikapy import TikapyClient
from tikapy import TikapySslClient

class SimpleQueues:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSimpleQueues(self):
        """
        Method will list all simple queues
        :return:
        """
        queue = self.client.talk(['/queue/simple/print'])
        if queue == {}:
            print("No queue found")
        else:
            print("Name\tTarget\tPacket-mark\tMax-limit")
            for i in queue:
                print(queue[i]['name']+"\t"+queue[i]['target']+"\t"+"\t"+queue[i]['packet-marks']+"\t"
                      +queue[i]['max-limit'])
        return queue

    def addQueue(self,interface):
        """
        Method will add new simple queue
        :param interface: interface to put
        :return:
        """
        queue = self.client.talk(['/queue/simple/add','=target='+interface])
        return queue

    def removeQueue(self,name):
        """
        Method will remove simple queue
        :param name: name of queue
        :return:
        """
        queue = self.client.talk(['/queue/simple/remove','=numbers='+name])
        return queue

    def enableQueue(self,name):
        """
        Method will enable simple queue
        :param name: name of queue
        :return:
        """
        queue = self.client.talk( ['/queue/simple/enable', '=numbers=' + name] )
        return queue

    def disableQueue(self,name):
        """
        Method will disable queue
        :param name: name of queue to disable
        :return:
        """
        queue = self.client.talk( ['/queue/simple/disable', '=numbers=' + name] )
        return queue

    def commentQueue(self,name,comment):
        """
        Method will comment queue
        :param name: name of queue to comment
        :param comment:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/comment', '=numbers=' + name,'=comment='+comment] )
        return queue

    def setName(self,name,Name):
        """
        Method will set name of current queue
        :param name:
        :param Name:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name,'=name='+Name] )
        return queue

    def setTarget(self,name,target):
        """
        Method will set new target
        :param name:
        :param target: address or interface
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=target=' + target] )
        return queue

    def setDestination(self,name,destination):
        """
        Method will set destionation on queue
        :param name:
        :param destination:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=dst=' + destination] )
        return queue


    def setMaxlimit(self,name,download="unlimited",uplaod="unlimited"):
        """
        Method will set max down uplaod
        :param name:
        :param download: 64k,128k,256k,384k,512k,768k,1M,2M,3M,4M,5M,10M
        :param uplaod:64k,128k,256k,384k,512k,768k,1M,2M,3M,4M,5M,10M
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=max-limit=' + uplaod + "/"+ download] )
        return queue

    def setBurstLimit(self,name,upload="unlimited",download="unlimited"):
        """
        Merhod will set bust limit uplaod download
        :param name:
        :param upload:
        :param download:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=burst-limit=' + upload + "/"
                                   + download] )
        return queue

    def setBurstTime(self,name,upload="0",download="0"):
        """
        Method will set upload and download for burst
        :param name:
        :param upload: in secs
        :param download: in secs
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=burst-time=' + upload + "/"
                                   + download] )

        return queue

    def setBurstThreshold(self,name,download="unlimited",upload="unlimited"):
        """
        Method will set burst threshold for download uplaod
        :param name:
        :param download:
        :param upload:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=burst-threshold=' + upload + "/"
                                   + download] )
        return queue
    def setTimeandDays(self,name,days,startTime="00:00:00",endTime="1d00:00:00"):
        """
        Method will set queue time
        :param name:
        :param startTime:
        :param endTime:
        :param days:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=time=' + startTime + "-" + endTime
                                   +","+days] )
        return queue

    #Advanced
    def setPacketMArk(self,name,mark):
        """
        Method will set packet mark
        :param name:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=packet-marks=' + mark] )
        return queue

    def setLimitAt(self,name,upload="unlimited",download="unlimited"):
        """
        Method will set limitations
        :param name:
        :param upload:
        :param download:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=limit-at=' +upload+"/"+download] )
        return queue

    def setPriority(self,name,upload="8",download="8"):
        """
        Method will set queue priority
        :param name:
        :param upload:
        :param download:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=priority=' +upload+"/"+download] )
        return queue

    def setBucketSize(self,name,upload="0.100",download="0.100"):
        """
        Method will set bucket size
        :param name:
        :param upload:
        :param download:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=bucket-size=' +upload+"/"+download] )
        return queue

    def setQueueType(self,name,download="default-small",upload="default-small"):
        """
        Method will set queue type
        :param name:
        :param download: default,default-small,ethernet-default,hotspot-default, multi-queue-ethernet-default,
        only-hardware-queue,pcq-download-default , pcq-upload-default, synchronous-default, wireless-default
        :param upload:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=queue=' + upload + "/" + download] )
        return queue

    def setParent(self,name,parent):
        """
        Method will set parent of queue
        :param name:
        :param parent:  none o r queue name
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=parent=' + parent] )
        return queue

    def setTotalLimitAt(self,name,limit):
        """
        Method will set total limux, less then max limit
        :param name:
        :param limit:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-limit-at=' + limit] )
        return queue

    def setTotalMaxLimit(self,name,limit):
        """
        Metjod will set max limit must be bigger then limit at
        :param name:
        :param limit:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-max-limit=' + limit] )
        return queue

    def setTotalPriority(self,name,priority):
        """
        Method will set total priority
        :param name:
        :param priority:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-priority=' + priority] )
        return queue

    def setTotalBurstTime(self,name,time):
        """
        Method will set total burst time, must be set before total busrt limit
        :param name:
        :param time: in secs
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-burst-time=' + time] )
        return queue

    def setTotalBurstThreshold(self,name,threshold):
        """
        Method will set total threshold
        :param name:
        :param threshold:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-burst-threshold=' + threshold] )
        return queue

    def setTotalBurstLimit(self,name,limit):
        """
        Method will set total limit, must be more then toal max limit
        :param name:
        :param limit: max limit
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-burst-limit=' + limit] )
        return queue

    def setTotalQueueType(self,name,type):
        """
        Method will set total queue type
        :param name:
        :param type:default,default-small,ethernet-default,hotspot-default, multi-queue-ethernet-default,
        only-hardware-queue,pcq-download-default , pcq-upload-default, synchronous-default, wireless-default
        :return:
        """
        queue = self.client.talk( ['/queue/simple/set', '=numbers=' + name, '=total-queue=' + type] )
        return queue

    def resetCounters(self,name):
        """
        Method will rest counters for simple queue
        :param name:
        :return:
        """
        queue = self.client.talk( ['/queue/simple/reset-counters', '=numbers=' + name] )
        return queue

    def resetAllCounters(self):
        """
        Method will reset all counters
        :return:
        """
        queue = self.client.talk( ['/queue/simple/reset-counters-all'] )
        return queue