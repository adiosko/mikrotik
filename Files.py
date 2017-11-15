from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint
import pexpect
import LoginManager
from paramiko import SSHClient
from scp import SCPClient

class Files:
    def __init__(self,address):
        self.client = TikapyClient( address, 8728 )
        self.client.login( 'admin', 'admin' )

    def listFiles(self):
        """
        method will list all files on mikrotik
        :return: list of files on mikrotik
        """
        files = self.client.talk(['/file/print'])
        print("File type\tCreation time\tName of file")
        for i in files:
            print(files[i]['type']+"\t"+files[i]['creation-time']+"\t"+files[i]['name'])
        return files

    def backupRouter(self,filename):
        """
        method will create backup file of curent config
        :param filename: name of the backup file you want to create
        :return: backup dictionary
        """
        backup = self.client.talk(['/system/backup/save','=name='+filename])
        return backup

    #dokoncit
    def loadBackup(self,filename,password,address):
        backup = self.client.talk(['system/backup/load','=name='+filename+"=password="+password])
        child = pexpect.spawn( address)
        child.expect("[y/N]")
        if child.sendline("y"):
            print("Restoring and rebooting the device")
        else:
            print("action cancelled")
        return backup

    def setBackupPassword(self,filename,password):
        """
        method will set password of current/new backup file of config
        :param filename: filename newbackup/existing backup file
        :param password: password of the file
        :return: backup files dictionary
        """
        backup = self.client.talk(['/system/backup/save','=name='+filename,'=password='+password])
        return backup

    def encryptBackup(self,filename):
        """
        method will encrypt config file
        :param filename: backup file name (new/existing)
        :return: backup dictionary
        """
        backup = self.client.talk(['/system/backup/save','=name='+filename,'=dont-encrypt=no'])
        return backup

    def decryptBackup(self,filename):
        """
        method will decrypt backup file (new/existing)
        :param filename: backup file name
        :return: backup dictionary
        """
        backup = self.client.talk(['/system/backup/save','=name='+filename,'=dont-encrypt=yes'])
        return backup

    #dokoncit
    def uploadFile(self,filepath,address,username,password):
        client = pexpect.spawn("scp "+filepath+" "+address+":/files")
        client.expect(username+"@"+address+"s password:")
        client.sendline(password)
        client.expect(pexpect.EOF, timeout=10)

    def exportConfig(self,filename):
        """
        method will export whole configuration file.rsc of mikrotik
        :param filename: rsc filename which will
        :return:
        """
        files = self.client.talk(['/export','=file='+filename])
        return files

    #opravit
    def importConfig(self,filename):
        """
        method will import file.rsc to current config
        :param filename:
        :return:
        """
        if filename:
            files = self.client.talk(['/import','=file-name='+filename,'=verbose=yes'])
        else:
            print("File does not exists")
        return files

    def downloadFile(self,filename):
        pass

