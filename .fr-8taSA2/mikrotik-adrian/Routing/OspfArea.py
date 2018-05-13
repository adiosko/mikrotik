from tikapy import TikapyClient
from tikapy import TikapySslClient

class OspfArea:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listAreas(self):
        """
        Method will list all areas
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/area/print'])
        if ospf == {}:
            print("No area defined")
        else:
            print("Name\tInstance\tArea ID\tType\tInterfaces\tActive ifaces\tNeighbors")
            for i in ospf:
                print(ospf[i]['name']+"\t"+ospf[i]['instance']+"\t"+ospf[i]['area-id']+"\t"+ospf[i]['type']+"\t"+
                      ospf[i]['interfaces']+"\t"+ospf[i]['active-interfaces']+"\t"+ospf[i]['adjacent-neighbors'])
        return ospf

    def addArea(self,instance="default"):
        """
        Method will add area by its instance
        :param instance:
        :return:
        """
        ospf = self.client.talk(['/routing/ospf/area/add','=instance='+instance])
        return ospf

    def removeArea(self,name):
        """
        Method will remove area
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/remove', '=numbers=' + name] )
        return ospf

    def disableArea(self,name):
        """
        Method will disable area
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/disable', '=numbers=' + name] )
        return ospf

    def enableArea(self,name):
        """
        Method will enable area
        :param name:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/enable', '=numbers=' + name] )
        return ospf

    def commentArea(self,name,comment):
        """
        Method will comment area
        :param name:
        :param comment:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/comment', '=numbers=' + name,'=comment='+comment] )
        return ospf

    def setAreaName(self,name,newName):
        """
        Method will rename area
        :param name:
        :param newName:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/set', '=numbers=' + name,'=name='+newName] )
        return ospf

    def setInstance(self,name,instance="default"):
        """
        Method will set instance
        :param name:
        :param instance:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/set', '=numbers=' + name, '=instance=' + instance] )
        return ospf

    def setAreaId(self,name,AID="0.0.0.0"):
        """
        Method willset area id
        :param name:
        :param AID:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/set', '=numbers=' + name, '=area-id=' + AID] )
        return ospf

    def setType(self,name,type="default"):
        """
        Method will set type of area
        :param name:
        :param type:
        :return:
        """
        ospf = self.client.talk( ['/routing/ospf/area/set', '=numbers=' + name, '=type=' + type] )
        return ospf