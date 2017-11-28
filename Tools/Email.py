from tikapy import TikapyClient
from tikapy import TikapySslClient

class Email:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listEmaoilSettings(self):
        """
        Method will list email settings
        :return: list
        """
        mail = self.client.talk(['/tool/e-mail/print'])
        if mail == {}:
            print("No settings found")
        else:
            for i in mail:
                print(mail)
        return mail
    def setEmails(self,server,port,tls,fromMail,user,password):
        """
        Method will set mail server
        :param server: IP where to send mail
        :param port: standard 25, or custom port
        :param tls: no (default)/ tls-only/yes
        :param fromMail: mail
        :param user: username
        :param password:password
        :return:list
        """
        mail = self.client.talk(['/tool/e-mail/set','=address='+server,'=port='+port,'=start-tls='+tls,
                                 '=from='+fromMail,'=user='+user,'=password='+password])
        return mail

    def sendEmail(self,address,port,user,password,tls,sendTo,fromUser,Subject,body,file=None,copy=None):
        """
        Method will send mail
        :param address: SMTP address
        :param port: 25
        :param user: username
        :param password: password
        :param tls: use tls yes/no/tls-only
        :param sendTo:mail to send
        :param copy: mail(m\optional)
        :param fromUser: source mail
        :param Subject: mail subject
        :param body: body of mail
        :param file:  file (optional)
        :return:
        """
        if file == None or copy == None:
            mail = self.client.talk(['/tool/e-mail/send','=server='+address,'=port='+port,'=user='+user,
                                     '=password='+password,'=start-tls='+tls,'=to='+sendTo,'=from='+fromUser,
                                     '=subject='+Subject,'=body='+body])
        else:
            mail = self.client.talk( ['/tool/e-mail/send', '=server=' + address, '=port='+port, '=user=' + user,
                                      '=password=' + password, '=start-tls='+ tls, '=to='+ sendTo,
                                      '=from=' + fromUser,'=subject=' + Subject, '=body=' + body,'=file='+file,
                                      '=cc='+copy])
        return mail