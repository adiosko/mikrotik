from tikapy import TikapyClient
from tikapy import TikapySslClient

class Console:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSystemConsoles(self):
        console = self.client.talk(['/system/console/print'])
        if console == {}:
            print("No console found")
        else:
            print("Disable\tVC#\tterminal")
            for i in console:
                print(console[i]['disabled']+"\t"+console[i]['vcno']+"\t"+console[i]['term'])
        return console

    def listTerminalScreen(self):
        """
        Method will list all terminal setup (not aplicable via api)
        :return: list
        """
        console = self.client.talk(['/system/console/screen/print'])
        print(console)
        return console

    def setTerminal(self,blankInterval,lines):
        """
        Method will setup mikrotik terminal
        :param blankInterval: 1min, 10min,60min,never
        :param lines: 25,40,50
        :return: list
        """
        terminal = self.client.talk(['/system/console/screen/set','=blank-interval='+blankInterval,'=line-count='+lines
                                     ])
        return terminal

    def addTerminal(self,name):
        """
        Method will add new terminal
        :param name: name of terminal f.e linux
        :return:
        """
        terminal = self.client.talk(['/system/console/add','=term='+name])
        return terminal