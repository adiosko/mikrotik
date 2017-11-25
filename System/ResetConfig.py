from tikapy import TikapyClient
from tikapy import TikapySslClient

class ResetConfig:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def resetConfig(self,keepConfig, noDeafult, CAPS = None, backup = None, run = None):
        """
        Method will reset configuration of router
        :param keepConfig: keepuser config after reset? yes/no
        :param noDeafult: keepNoDefaultConfig yes/no
        :param CAPS:  keep caps (optional)
        :param backup: (optional) skip backup
        :param run: run file after reboot
        :return:  list
        """
        if CAPS == None or backup == None or run == None:
            reset = self.client.talk(['/system/reset-configuration','=keep-users='+keepConfig,'=no-defaults='+noDeafult
                                      ])
        else:
            reset = self.client.talk(['/system/reset-configuration','=keep-users='+keepConfig,'=no-defaults='+noDeafult
                                      ,'=caps-mode='+CAPS,'=skip-backup='+backup, '=run-after-reset'+run])
        return reset