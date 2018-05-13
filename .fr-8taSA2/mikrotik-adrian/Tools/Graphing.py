from tikapy import TikapyClient
from tikapy import TikapySslClient

class Graphing:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listGraphing(self):
        """
        Method will list all graphing
        :return: list
        """
        graph = self.client.talk(['/tool/graphing/print'])
        if graph == {}:
            print("Cannot find grpahing settings or api is not collable")
        else:
            for i in graph:
                print(graph)
        return graph

    def setGraphing(self,storeInterval):
        """
        Method will set store interval
        :param storeInterval: 5min,24hours,hour
        :return: list
        """
        graf = self.client.talk(['/tool/graphing/set','=store-every='+storeInterval])
        return graf

    def listInterfaceRules(self):
        """
        method will list all interface rules
        :return:  list
        """
        iface = self.client.talk(['/tool/graphing/interface/print'])
        if iface == {}:
            print("Empty rules")
        else:
            print("Interface\tAllow address\tstore on disk")
            for i in iface:
                print(iface[i]['interface']+"\t"+iface[i]['allow-address']+"\t"+iface[i]['store-on-disk'])
        return iface

    def addInterfaceRule(self,interface,allowAddress,storeOnDisk):
        """
        Method will set interface rule
        :param interface: interface : all, or speific  interface f.e ether1
        :param allowAddress: f.e 0.0.0.0/0
        :param storeOnDisk: yes/no
        :return: list
        """
        iface = self.client.talk(['/tool/graphing/interface/add','=interface='+interface,'=allow-address='+allowAddress,
                                  '=store-on-disk='+storeOnDisk])
        return iface

    def removeInterfaceRule(self,number):
        """
        Method will remove interface from interface list
        :param number: number of rule
        :return: list
        """
        iface = self.client.talk(['/tool/graphing/interface/remove','=numbers='+number])
        return iface

    def listQueueRules(self):
        """
        Method will list all queue rules
        :return: list
        """
        queue = self.client.talk(['/tool/graphing/queue/print'])
        if queue == {}:
            print("No queue rule found")
        else:
            print("Simplequeue\tallowAddress\tstoreOnDisk\tallowTarget")
            for i in queue:
                print(queue[i]['simple-queue']+"\t"+queue[i]['allow-address']+"\t"+queue[i]['store-on-disk']+
                      "\t"+queue[i]['allow-target'])
        return queue

    def addQueueRule(self,simpleQueue,allowAddress,storeOnDisk,allowTarget):
        """
        Method will add queue rules to mikrotik
        :param simpleQueue:  all
        :param allowAddress:  address
        :param storeOnDisk: yes/no
        :param allowTarget: yes/no
        :return:  list
        """
        queue = self.client.talk(['/tool/graphing/queue/add','=simple-queue='+simpleQueue,'=allow-address='+allowAddress,
                                  '=store-on-disk='+storeOnDisk,'=allow-target='+allowTarget])
        return queue

    def removeQueueRule(self,number):
        """
        Method will remove rule under its number
        :param number: number of rule
        :return:  list
        """
        queue = self.client.talk(['/tool/graphing/queue/remove','=numbers='+number])
        return queue

    def listResourceRules(self):
        """
        Method will list all resource lists
        :return: list
        """
        resor = self.client.talk(['/tool/graphing/resource/print'])
        if resor == {}:
            print("No rule found")
        else:
            print("Allow address\tStore on disk")
            for i in resor:
                print(resor[i]['allow-address']+"\t"+resor[i]['store-on-disk'])
        return resor

    def addResourceRule(self,allowAddress,StoreOnDisk):
        """
        Method will add resource rule
        :param allowAddress: address to allow
        :param StoreOnDisk: yes/no
        :return: list
        """
        resor = self.client.talk(['/tool/graphing/resource/add','=allow-address='+allowAddress,'=store-on-disk='
                                  +StoreOnDisk])
        return resor

    def removeResourceRule(self,number):
        """
        Method will remove resource rule
        :param number: number of rule
        :return: list
        """
        resor = self.client.talk(['/tool/graphing/resource/remove','=numbers='+number])
        return resor