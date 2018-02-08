from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecProposal:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listProposal(self):
        """
        Method will list proposal
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/proposal/print'])
        print("Name\tauth alg\tenc alg\tlifetime\tpfs group")
        for i in ipsec:
            print(ipsec[i]['name']+"\t"+ipsec[i]['auth-algorithms']+"\t"+ipsec[i]['enc-algorithms']+"\t"+ipsec[i]['lifetime']+"\t"+ipsec[i]['pfs-group'])
        return ipsec

    def addProposal(self,name,auth="sha1",enc="3des"):
        """
        Method will add proposal
        :param name:
        :param auth:md5,sha1,null,sha256,sha512
        :param enc: null, des,aes-192-cbc,aes-128-cbc,aes-256-cbc,blowfish,twofish,camelia-128,camelia-192,camelia-256,aes-128-ctr,
        aes-192-ctr,aes-256-ctr,aes-128-gcm,aes-192-gcm,aes-256-gcm
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/proposal/add','=name'+name,'=auth-algorithms','=enc-algorithms'])
        return ipsec

    def removeProposal(self,name):
        """

        :param name:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/proposal/remove','=numbers='+name])
        return ipsec

    def enableProposal(self,name):
        """

        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/enable', '=numbers=' + name] )
        return ipsec

    def disableProposal(self,name):
        """
        Method will disable proposal
        :param name:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/disable', '=numbers=' + name] )
        return ipsec

    def setName(self,name,newName):
        """
        Method will rename proposal
        :param name:
        :param newName:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/set', '=numbers=' + name,'=name='+newName] )
        return ipsec

    def setAuthAlgo(self,name,auth="sha1"):
        """
        Methodwill set authatication algorithm
        :param name:
        :param auth: md5,sha1,null,sha256,sha512
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/set', '=numbers=' + name, '=auth-algorithms=' + auth] )
        return ipsec

    def setEncAlg(self,name,enc="3des"):
        """
        Method will set encrypton algorithms
        :param name:
        :param enc: null, des,aes-192-cbc,aes-128-cbc,aes-256-cbc,blowfish,twofish,camelia-128,camelia-192,camelia-256,aes-128-ctr,
        aes-192-ctr,aes-256-ctr,aes-128-gcm,aes-192-gcm,aes-256-gcm
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/set', '=numbers=' + name, '=enc-algorithms=' + enc] )
        return ipsec

    def setLifeTime(self,name,life="00:30:00"):
        """
        Method will set proposal lifetime
        :param name:
        :param life:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/set', '=numbers=' + name, '=lifetime=' + life] )
        return ipsec

    def setPfsGroup(self,name,group="modp2048"):
        """
        Method will set pfs group
        :param name:
        :param group: modp768,modp1024,ec2n155,ec2n185,modp1536,modp2048,modp3072,modp4096,modp6144,modp8192, none
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/proposal/set', '=numbers=' + name, '=pfs-group=' + group] )
        return ipsec

