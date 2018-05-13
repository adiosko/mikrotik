from tikapy import TikapyClient
from tikapy import TikapySslClient

class SMS:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def enableSMS(self,port):
        """
        Method will enable sms server
        :param port: sms port
        :return: list
        """
        sms = self.client.talk(['/tool/sms/set','=receive-enabled=yes','=port='+port])
        return sms

    def disableSMS(self):
        """
        Method will disable sms server
        :return: list
        """
        sms = self.client.talk(['/tool/sms/set','=receive-enabled=no'])
        return sms

    def setChannel(self,channel):
        """
        Method will set channel number
        :param channel: channel number
        :return: list
        """
        chanel = self.client.talk(['/tool/sms/set','=channel='+channel])
        return chanel

    def setSecret(self,secret):
        """
        Method will set sms password
        :param secret: secret of sms
        :return: list
        """
        secret = self.client.talk( ['/tool/sms/set', '=secret=' +secret] )
        return secret

    def setAllowedNumber(self,number):
        """
        Method will set allowed number
        :param number: numbe to allow
        :return: list
        """
        number = self.client.talk( ['/tool/sms/set', '=allowed-number=' + number] )
        return number

    def setMaxSms(self,maximum):
        """
        Method will set maximum amount of sms
        :param maximum: maximum amount of sms messages
        :return: list
        """
        sms = self.client.talk( ['/tool/sms/set', '=keep-max-sms=' + maximum] )
        return sms

    def listSmsSettings(self):
        """
        Method will list sms settings
        :return:
        """
        sms = self.client.talk( ['/tool/sms/print'] )
        print(sms)
        return sms

    def listInbox(self):
        """
        Method will list message inbox
        :return:
        """
        chanel = self.client.talk( ['/tool/sms/inbox/print'] )
        return chanel

    def removeSms(self,number):
        """
        Method will remove message by its number
        :param number: message number
        :return: list
        """
        chanel = self.client.talk( ['/tool/sms/remove', '=numbers=' + number] )
        return chanel

    def sendMessage(self,port,number,message):
        """
        Method will send sms message
        :param port: port number
        :param number: number to send
        :param message: message to send
        :return:
        """
        chanel = self.client.talk( ['/tool/sms/send', '=phone-number=' + number,'=message='+message,
                                    '=port='+port] )
        return chanel
