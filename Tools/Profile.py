from tikapy import TikapyClient
from tikapy import TikapySslClient

class Profile:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setProfile(self,file,interval):
        """
        Method will set hw monitoring to file
        :param file: filename
        :param interval: tme of elapsation
        :return:
        """
        prof = self.client.talk(['/tool/profile','=file-name='+file,'=duration='+interval])
        return prof