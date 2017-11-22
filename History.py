from tikapy import TikapyClient
from tikapy import TikapySslClient

class History:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listHistory(self):
        hist = self.client.talk(['/system/history/print'])
        print('time\taction\tby\tpolicy')
        for i in hist:
            print(hist[i]['time']+"\t"+hist[i]['action']+"\t"+hist[i]['by']+"\t"+hist[i]['policy'])
        return hist