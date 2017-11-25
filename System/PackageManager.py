from tikapy import TikapyClient
from tikapy import TikapySslClient

class PackageManager:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username, password )

    def listPackages(self):
        """
        method will list all available packages on mikrotik
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/print'])
        print(packages)
        print("build-time \t package name \t package version \t disable status \t Scheduled status")
        for i in packages:
            print(packages[i]['build-time']+"\t"+packages[i]['name']+"\t"+packages[i]['version']+"\t"+packages[i]
            ['disabled']+"\t"+packages[i]['scheduled'])
        return packages

    def enablePackage(self,packagename):
        """
        method will enable disabled package by calling its name
        :param packagename: name of the package you want to enable
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/enable','=numbers='+packagename])
        return packages

    def disablePackage(self,packagename):
        """
        method will disable enabled package
        :param packagename: package you want to disable
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/disable','=numbers='+packagename])
        return packages

    def unschedulePackageDisable(self,packagename):
        """
        method will unschedule disablement
        :param packagename: name of package you want to un-disable
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/unschedule','=numbers='+packagename])
        return packages

    def packageDowngrade(self):
        """
        method will downgrade system packages
        :return: list of system packages
        """
        packages = self.client.talk(['/system/package/downgrade'])
        return packages

    def unninstalPackage(self,packagename):
        """
        method will schedule the unninstalation after the device reboot via its package name
        :param packagename: name of the package you want to remove
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/uninstall','=numbers='+packagename])
        return packages

    def exportPackageConfiguration(self,filename):
        """
        method will export configuration of packages configuration to a file.rsc, to verify  use Files library to
        verify it
        :param packagename: name of the file you wanna export configuration to
        :return: list of packages
        """
        packages = self.client.talk(['/system/package/export','=file='+filename])
        return packages

    def installPackageUpdate(self):
        """
        method will update packages on mikrotik
        :return: list of packages words
        """
        packages = self.client.talk(['/system/package/update/install'])
        print(packages)
        return packages

    def checkforupdates(self):
        """
        method will check for packages updates online
        :return: result of api words
        """
        packages = self.client.talk(['/system/package/update/check-for-updates'])
        print(packages)
        return packages

    def checkInstalation(self):
        """
        method will check mikrotik installation
        :return: output of results
        """
        instal = self.client.talk(['/system/check-installation'])
        print(instal)
        return instal

    def checkDisk(self):
        """
        method will check disk on  mikrotik after device reboot
        :return: result of api
        """
        disk = self.client.talk(['/system/check-disk'])
        print(disk)
        return disk







