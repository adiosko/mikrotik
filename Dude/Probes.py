from tikapy import TikapyClient
from tikapy import TikapySslClient

class Probes:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listProbes(self):
        """
        Method will list all probes on mikrotik
        :return: list
        """
        prob = self.client.talk(['/dude/probe/print'])
        if prob == {}:
            print("Nothing found")
        else:
            print("Name")
            for i in prob:
                print(prob[i]['name'])
        return prob

    def addProbe(self,name):
        """
        Method will add new probe by its name
        :param name: name of probe
        :return: list
        """
        probe = self.client.talk(['/dude/probe/add','=name='+name])
        return probe

    def setProbe(self,name,newName):
        """
        Method will rename custom probe
        :param name: ol name of probe
        :param newName: new name of probe
        :return: list
        """
        probe = self.client.talk(['/dude/probe/set','=numbers='+name,'=name='+newName])
        return probe

    def removeProbe(self,name):
        """
        Method will remove probe
        :param name: name of probe to remove
        :return: list
        """
        probe = self.client.talk(['/dude/probe/remove','=numbers='+name])
        return probe

