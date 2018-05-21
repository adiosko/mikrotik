from tikapy import TikapyClient
from tikapy import TikapySslClient

class AutoUpdate:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listSystemUpgradePackages(self):
        """
        Method will list all updates downlaaded
        :return: lisf of updates
        """
        update = self.client.talk(['/system/upgrade/print'])
        if update == {}:
            print("No update files found")
        else:
            print(update)
        return update

    def downloadSpecificUpdateFile(self,fileName):
        """
        Method will download specific update by its name
        :param fileName: name of package u wanna download
        :return:  list of packages
        """
        files = self.client.talk(['/system/upgrade/download','=numbers='+fileName])
        return files

    def downloadUpdates(self):
        """
        Method will download all updates to mikrotik
        :return:  list of updates
        """
        files = self.client.talk( ['/system/upgrade/download-all'] )
        return files

    def listUpdateSources(self):
        """
        Method will list all update sources
        :return: list of sources
        """
        sources = self.client.talk(['/system/upgrade/upgrade-package-source/print'])
        if sources == {}:
            print("No source found")
        else:
            print("Address\tUsername")
            for i in sources:
                print(sources[i]['address']+" "+sources[i]['user'])
        return sources

    def addDownloadSource(self,address,username):
        """
        Method will add Download source by address and username
        :param address: source address (IP)
        :param username: source username
        :return: list of words
        """
        source = self.client.talk(['/system/upgrade/upgrade-package-source/add','=address='+address,'=user='+username])
        return source

    def setDownloadMirror(self,enabled,server1,server2,interval,username,password):
        """
        Method will setup Download MIrror
        :param enabled:  enable status yes or no
        :param server1: IP of primary server
        :param server2: IP of secondary server
        :param interval: interval of checking
        :param username: username on server
        :param password: password on server
        :return: list
        """
        mirror = self.client.talk(['/system/upgrade/mirror/set','=enabled='+enabled
                                   ,'=primary-server='+server1,'=secondary-server='+server2,'=check-interval='+interval
                                   ,'=user='+username,'=password='+password])
        return mirror

    def listMirrors(self):
        """
        Method will list setup mirrors to download packages
        :return: list
        """
        mirror = self.client.talk(['/system/upgrade/mirror/print'])
        print(mirror)
        return mirror
