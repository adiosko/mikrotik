from tikapy import TikapyClient
from tikapy import TikapySslClient

class QueueTypes:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listQueueTypes(self):
        """
        Method will list queue types
        :return:
        """
        queue = self.client.talk(['/queue/type/print'])
        if queue == {}:
            print("No queue found")
        else:
            print("Queue type name \t Kind of queue")
            for i in queue:
                print(queue[i]['name']+"\t"+queue[i]['kind'])
        return queue

    def addQueue(self,name,type="pfifo"):
        """
        Method will add new queue type
        :param name:
        :param type: bfifo, mq-pfifo,none,pcq,pfifo,red,sfq
        :return:
        """
        queue = self.client.talk(['/queue/type/add','=name='+name,'=kind='+type])
        return queue

    def removeQueueType(self,name):
        """
        Method will remove queue type
        :param name:
        :return:
        """
        queue = self.client.talk(['/queue/type/remove','=numbers='+name])
        return queue

    #nastavenie queue types
    # names cannot be changed
    def setKind(self,name,kind):
        """
        Method will set new kind of default values
        :param name:
        :param kind: pfifo,sfq,mq-pfifo,none,pcq,red,bfifo
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name,'=kind='+kind] )
        return queue

    def setPfifoQueueSize(self,name,size):
        """
        Method will set queue size for specific method of pfifo
        :param name: default, default-small, ethernet-default
        :param size: 50 default
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name,'=kind=pfifo','=pfifo-limit='+size] )
        return queue

    def setSfqPerturb(self,name,perturb="5"):
        """
        Method will set sfq perturb hotspot-default
        :param name:
        :param perturb: in secs def 5
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=sfq', '=sfq-perturb=' + perturb] )
        return queue

    def setSfqAllot(self,name,allot="1514"):
        """
        Method will set pcq allot hotspot-default
        :param name: name of pcq queue type
        :param allot: 1514 bytes def
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=sfq', '=sfq-allot=' +allot] )
        return queue

    def setMqPfifoQueueSize(self,name,size="50"):
        """
        Method will set new queue size of mq pfifo what is multi-queue-ethernet-default
        :param name:
        :param size: def 50 packets
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=mq-pfifo', '=mq-pfifo-limit=' + size] )
        return queue

    def setPcqRate(self,name,rate="0"):
        """
        Method will set pcq rate in b/s
        :param name: pcq-download-default, pcq-upload-default
        :param rate: 0 default
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-rate=' + rate] )
        return queue

    def setPcqLimit(self,name,limit="50"):
        """
        Method will set pcq limit
        :param name:  pcq-download-default, pcq-upload-default
        :param limit: def 50 KB
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-limit=' + limit] )
        return queue

    def setPcqTotalLImit(self,name,limit="2000"):
        """
        Method will set pcq total limit
        :param name:
        :param limit: 2000 KB
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-total-limit=' + limit] )
        return queue

    def setPcqBurstSize(self,name,rate="0"):
        """
        Method will set burst size
        :param name:
        :param rate:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-burst-rate=' + rate] )
        return queue

    def  setPcqBurstThreshold(self,name,threshold="0"):
        """
        Method will set burst threshold
        :param name:
        :param threshold: def 0
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-burst-threshold='
                                   + threshold] )
        return queue

    def setPcqBurstTime(self,name,time="00:00:10"):
        """
        Methdd will set pcq burst time
        :param name:
        :param time: def 00:00:10 s
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-burst-time=' + time] )
        return queue

    def setPcqSrcAddressClassifier(self,name):
        """
        Method will set src address classifier
        :param name:
        :param classifier:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-classifier=src-address'] )
        return queue

    def setPcqDstAddressClassifier(self, name):
        """
        Method will set src address classifier
        :param name:
        :param classifier:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-classifier=dst-address'] )
        return queue

    def setPcqSrcPortClassifier(self, name):
        """
        Method will set src address classifier
        :param name:
        :param classifier:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-classifier=src-port'] )
        return queue

    def setPcqDstPortClassifier(self, name):
        """
        Method will set src address classifier
        :param name:
        :param classifier:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-classifier=dst-port'] )
        return queue

    def setPcqSrcAddressMaskLength(self,name,length="32"):
        """
        Method will set pcq src address length in bits
        :param name:
        :param length: max 32 def
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-src-address-mask='+length] )
        return queue

    def setPcqDstAddressMaskLength(self, name, length="32"):
        """
        Method will set pcq src address length in bits
        :param name:
        :param length: max 32 def
        :return:
        """
        queue = self.client.talk(['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-dst-address-mask=' + length] )
        return queue

    def setPcqSrcAddress6MaskLength(self, name, length="128"):
        """
        Method will set pcq src address length in bits
        :param name:
        :param length: max 32 def
        :return:
        """
        queue = self.client.talk(['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-src-address6-mask=' + length] )
        return queue

    def setPcqDstAddress6MaskLength(self, name, length="128"):
        """
        Method will set pcq src address length in bits
        :param name:
        :param length: max 32 def
        :return:
        """
        queue = self.client.talk(['/queue/type/set', '=numbers=' + name, '=kind=pcq', '=pcq-dst-address6-mask=' + length] )
        return queue

    def setRedQueueSize(self,name,size="60"):
        """
        Method will set red queue size
        :param name: synchronous-default
        :param size: 60 packets def
        :return:
        """
        queue = self.client.talk(['/queue/type/set','=numbers='+name,'=red-limit='+size])
        return queue

    def setRedMinimalThreshold(self,name,hold="10"):
        """
        Method will set minimal threshold in packets
        :param name: synchronous-default
        :param hold:
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=red-min-threshold=' + hold] )
        return queue

    def setRedMaximumThreshold(self,name,hold="50"):
        """
        Method will set maximum threshold
        :param name:
        :param hold: 50 packets default
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=red-max-threshold=' + hold] )
        return queue

    def setRedBurst(self,name,burst="20"):
        """
        Method will set default red burst
        :param name:
        :param burst: 20 packets default
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=red-burst=' + burst] )
        return queue

    def setRedAveragePacketSize(self,name,packetSize="1000"):
        """
        Method will set packet size
        :param name:
        :param packetSize: def 1000 bytes
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=red-avg-packet=' + packetSize] )
        return queue

    def setBfifoSize(self,name,QueueSize="1500"):
        """
        Method will set bfifo size
        :param name:
        :param QueueSize: def 1500 bytes
        :return:
        """
        queue = self.client.talk( ['/queue/type/set', '=numbers=' + name, '=bfifo-limit=' + QueueSize] )
        return queue