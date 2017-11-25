from tikapy import TikapyClient
from tikapy import TikapySslClient

class Scripts:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listScripts(self):
        """
        Method will list all custom scripts
        :return: list
        """
        script = self.client.talk(['/system/script/print'])
        if script == {}:
            print("No script found")
        else:
            print("Name\tOwner\tLast Time Started \t Run Count")
            for i in script:
                print(script[i]['name']+"\t"+script[i]['owner']+"\t"+script[i]['last-started'])
        return script

    def addScript(self,name,policy):
        """
        Method will add script by its name and policy
        :param name: name of script
        :param policy: policy to apply ftp, read, policy, password, sensitive, dude, reboot, write, test, sniff, romon
        :return: list
        """
        src = self.client.talk(['/system/script/add','=name='+name,'=policy='+policy])
        return src

    def setScript(self,name,policy):
        """
        Method will set existing policy of script
        :param name: name of existing script
        :param policy: policy to setup
        :return:
        """
        src = self.client.talk(['/system/script/set','=numbers='+name,'=policy='+policy])
        return src

    def removeScript(self,name):
        """
        Method will remove  script
        :param name: name of script
        :return: list
        """
        src = self.client.talk( ['/system/script/remove', '=numbers=' + name] )
        return src

    def runScript(self,name):
        """
        Method woll run script by its name
        :param name: name of script
        :return:
        """
        src = self.client.talk(['/system/script/run','=number='+name])

    def listENvinroment(self):
        """
        Method will list envinroment
        :return: list
        """
        env = self.client.talk(['/system/script/environment/print'])
        if env == {}:
            print("No env found")
        else:
            print("Name\tValue")
            for i in env:
                print(env[i]['name']+"\t"+env[i]['value'])
        return env

    def setEnvinroment(self,name,value):
        """
        Method will setup env for custom value
        :param name: name of env
        :param value: new value
        :return: list
        """
        env = self.client.talk(['/system/script/environment/set','=numbers='+name,'=value='+value])
        return env

    def removeEnvironment(self,name):
        """
        Method will remove env
        :param name: name of env to remove
        :return: list
        """
        env = self.client.talk(['/system/script/environment/remove','=numbers='+name])
        return env

    def listJobs(self):
        """
        Method will list all jobs on mikrotik
        :return: list
        """
        env = self.client.talk(['/system/script/job/print'])
        if env == {}:
            print("No job found")
        else:
            print("POlicy\t\t\t\tstarted\towner")
            for i in env:
                print(env[i]['policy']+"\t"+env[i]['started']+"\t"+env[i]['owner'])
        return env

    def setJobs(self,name,type):
        """
        Method will change job type
        :param name: name of job u wanna set
        :param type: type of job:api-login, command, login
        :return: list
        """
        env = self.client.talk(['/system/script/job/set','=numbers='+name,'=type='+type])
        return env

    def removeJob(self,name):
        """
        Method will remove job
        :param name: name of jopb to remove
        :return: list
        """
        env = self.client.talk(['/system/script/job/remove','=numbers='+name])
        return env