from tikapy import TikapyClient
from tikapy import TikapySslClient

class Tftp:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listTftp(self):
        """
        Method will list tftps
        :return:
        """
        tftp = self.client.talk(['/ip/tftp/print'])
        print("IP\tReq filename\tReal filename\tallow\treadonly\thits")
        for i in tftp:
            print(tftp[i]['ip-addresses']+"\t"+tftp[i]['req-filename']+"\t"+tftp[i]['real-filename']+"\t"+tftp[i]['allow']+"\t"+tftp[i]['read-only']+"\t"+tftp[i]['hits'])
        return tftp

    def addTftp(self,server):
        """
        Method will add tftp server
        :param server:
        :return:
        """
        tftp = self.client.talk(['/ip/tftp/add','=ip-addresses='+server])
        return tftp

    def removeTftp(self,number):
        """
        Method will remove tftp server
        :param number:
        :return:
        """
        tftp = self.client.talk(['/ip/tftp/remove','=numbers='+number])
        return tftp

    def enableTftp(self, number):
        """
        Method will enable tftp server
        :param number:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/enable', '=numbers=' + number] )
        return tftp

    def disableTftp(self, number):
        """
        Method will remove tftp server
        :param number:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/disable', '=numbers=' + number] )
        return tftp

    def setServer(self,number,server):
        """
        Method will se ttftp server IP
        :param number:
        :param server:
        :return:
        """
        tftp = self.client.talk(['/ip/tftp/set','=numbers='+number,'=ip-addresses='+server])
        return tftp

    def setRequestedFile(self,number,fileName):
        """
        Method will set req file name
        :param number:
        :param fileName:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/set', '=numbers=' + number, '=req-filename=' + fileName] )
        return tftp

    def setRealFileName(self,number,fileName):
        """
        Method will set  real  file name
        :param number:
        :param fileName:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/set', '=numbers=' + number, '=real-filename=' + fileName] )
        return tftp

    def setAllow(self,number):
        """
        Method will set allow
        :param number:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/set', '=numbers=' + number, '=allow=yes'] )
        return tftp

    def setReadOnly(self,number):
        """
        Method will set read only file
        :param number:
        :return:
        """
        tftp = self.client.talk( ['/ip/tftp/set', '=numbers=' + number, '=read-only=yes'] )
        return tftp

    