from tikapy import TikapyClient
from tikapy import TikapySslClient
from pprint import pprint
import pexpect
import LoginManager
from paramiko import SSHClient
from scp import SCPClient
import os

class Files:
    def __init__(self,address,username,password):
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

    def backupRouter(self):
        """
        mathod will backup router without naming using system name identity-date.backup
        :return: return files
        """
        backup = self.client.talk(['/system/backup/save'])
        return backup

    def backupRouterwithSpecificFilename(self,filename):
        """
        method will create backup file of curent config with specific name
        :param filename: name of the backup file you want to create
        :return: backup dictionary
        """
        backup = self.client.talk(['/system/backup/save','=name='+filename])
        return backup

        # dokoncit
    def loadBackup(self, filename, password):
        """
        method will restore mikrotik config via backup file (backup.backup for exmaple)
        :param filename: filename.backup created by backuRouter method
        :param password: password of backup file, if none use ""
        :return: backup files
        """
        backup = self.client.talk( ['/system/backup/load', '=name=' + filename, '=password=' + password] )
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


    def uploadFile(self,username,password,filepath,destinationfilename,host):
        """
        method will upload file from local machine to mikrotik
        :param username: username on the router
        :param password: password of the pushed username
        :param filepath: path to file on local machine
        :param destinationfilename: filename which you want to use on mikrotik file tree
        :param host: IP address of the device
        :return: return operation status
        """
        upload = os.system("sshpass -p "+password+" scp "+filepath+" "+username+"@"+host+":"+destinationfilename)
        return upload

    def downloadFile(self, username,password,filename,destinationfilepath,host):
        """
        method will download file frok mikrotik to local machine
        :param username: username on mikrotik
        :param password: password on mikrotik
        :param filename: file name, which you want to download
        :param destinationfilepath: path, where to download the file to your machine
        :param host: IP address of mikrotik
        :return: return operation status
        """
        download = os.system("sshpass -p "+password+" scp "+username+"@"+host+":"+filename+" "+destinationfilepath)
        return download
    #falling method
    def exportConfig(self,filename):
        """
        method will export whole configuration file.rsc of mikrotik
        :param filename: rsc filename which will
        :return: return files
        """
        files = self.client.talk(['/export','=file='+filename])
        return files

    #opravit
    """
    def importConfig(self,filename):
        method will import file.rsc to current config
        :param filename:
        :return:
        if filename:
            files = self.client.talk(['/import','=file-name='+filename,'=verbose=yes'])
        else:
            print("File does not exists")
        return files
    """




