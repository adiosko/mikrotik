from tikapy import TikapyClient
from tikapy import TikapySslClient

class Scheduller:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listSystemTasks(self):
        """
        Method will list all system tasks schedulled
        :return: list
        """
        schd = self.client.talk(['/system/scheduler/print'])
        if schd == {}:
            print("No scheduled task found")
        else:
            print("Disabled\tName\tStart Date\tStart Time\tInterval\tOwner\tRun COunt\tnext run")
            for i in schd:
                print(schd[i]['disabled']+"\t"+schd[i]['name']+"\t"+schd[i]['start-time']
                      +"\t"+schd[i]['interval']+"\t"+schd[i]['owner']+"\t"+schd[i]['run-count'])
        return schd

    def addNewTask(self,name,disabled, startTime, startDay,policy,interval):
        """
        Method will add new scheduled task
        :param name: name of task
        :param disabled: enabled or no
        :param startTime:  f.e 19:04:22
        :param startDay: Nov/25/2017 f.e
        :param policy: ftp, read, policy, password, sensitive, dude, reboot, write, test, sniff, romon
        :param interval: 00:00:00
        :return: list
        """
        task = self.client.talk(['/system/scheduler/add','=name='+name,'=disabled='+disabled,'=start-time='+startTime,
                                 '=start-date='+startDay,'=policy='+policy,'=interval='+interval])
        return task

    def removeTask(self,name):
        """
        Method will remove task
        :param name: name of task
        :return: list
        """
        task = self.client.talk(['/system/scheduler/remove','=numbers='+name])
        return name

    def enableTask(self,name):
        """
        Method will enable task
        :param name: name of task to enable
        :return: list
        """
        ena = self.client.talk(['/system/schedule/enable','=numbers='+name])
        return ena

    def disableTask(self,name):
        """
        Method will disable task
        :param name: name of task to disable
        :return: list
        """
        dis = self.client.talk(['/system/schedule/disable','=numbers='+name])
        return dis

