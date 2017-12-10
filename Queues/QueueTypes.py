from tikapy import TikapyClient
from tikapy import TikapySslClient

class QueueTypes:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
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

    #nastavenie queue types default

