from tikapy import TikapyClient
from tikapy import TikapySslClient

class WatchDog:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username, password )

    def listWatchdogs(self):
        """
        Method will list all watchdogs
        :return: list
        """
        wdg = self.client.talk(['/system/watchdog/print'])
        print(wdg)
        return wdg

    def setWatchdog(self,watchAddr=None,watchTimer=None,NoPingDelay=None,autoSupport=None,autoSuppOut=None):
        """
        Method will set watchdogs
        :param watchAddr: address of watchdogs
        :param watchTimer: def yes yes/no
        :param NoPingDelay: def 5s
        :param autoSupport: yes def
        :param autoSuppOut: no default
        :return: list
        """
        if watchAddr==None or watchTimer==None or NoPingDelay == None or autoSupport == None or autoSuppOut == None:
            print("No parameter to setup")
        else:
            wdg = self.client.talk(['/system/watchdog/set','=watch-address='+watchAddr,'=watchdog-timer='+watchTimer
                                    ,'=no-ping-delay='+NoPingDelay,'=automatic-supout='+autoSupport,'=auto-send-supout='+
                                    autoSuppOut])
        return wdg

    def setWatchdogEmail(self,EmailTo,EmailFrom):
        """
        Method will setup watchdog mail
        :param EmailTo: email to
        :param EmailFrom: email from
        :return: list
        """
        wdg = self.client.talk(['/system/watchdog/set','=send-email-to='+EmailTo,'=send-email-from='+EmailFrom])
        return wdg

    def setSMTPServer(self,smtpServer):
        """
        Method will setup SNMP server
        :param snmpServer: IP of server
        :return: list
        """
        wdg = self.client.talk(['/system/watchdog/set','=send-smtp-server='+smtpServer])
        return wdg
