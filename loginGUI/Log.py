from tikapy import TikapyClient
from tikapy import TikapySslClient

class Log:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listLog(self):
        """
        Method will print log
        :return:
        """
        log = self.client.talk(['/log/print'])
        if log == {}:
            print("No log found")
        else:
            print("time\ttopics\tmassage")
            for i in log:
                print(log[i]['time']+"\t"+log[i]['topics']+"\t"+log[i]['message'])
        return log
