from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecKeys:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listKeys(self):
        """
        Method will list keys
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/key/print'])
        print("Name\tSize")
        for i in ipsec:
            print(ipsec[i]['name']+"\t"+ipsec[i]['key-size'])
        return ipsec

    def removeKey(self,name):
        """
        Method will remove key
        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/key/remove','=numbers='+name])
        return ipsec

    def importKey(self,fileName):
        """
        Method will import key
        :param fileName: absolute path to file i.e /etc/ssh/crt.key
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/key/import', '=file-name=' + fileName] )
        return ipsec

    def exportPublicKey(self,keyCert,fileName):
        """
        Method will export key
        :param keyCert: key to export
        :param fileName: save as file
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/key/export-pub-key','=key='+keyCert, '=file-name=' + fileName] )
        return ipsec

    def generateKey(self,name):
        """
        Method will generate key
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/key/generate-key', '=name=' + name] )
        return ipsec

    def setName(self,name,newName):
        """
        Method will rename key
        :param name:
        :param newName:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/key/set','=numbers='+name,'=name='+newName])
        return ipsec

    def setKeySize(self,name,keySize="1024"):
        """
        Method will set public key size
        :param name:
        :param keySize: 1024,2048,4196
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/key/set', '=numbers=' + name, '=key-size=' + keySize] )
        return ipsec

    

