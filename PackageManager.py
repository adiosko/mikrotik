from tikapy import TikapyClient
from tikapy import TikapySslClient

class PackageManager:
    def __init__(self,address):
        self.client = TikapyClient( address, 8728 )
        self.client.login( 'admin', 'admin' )

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






