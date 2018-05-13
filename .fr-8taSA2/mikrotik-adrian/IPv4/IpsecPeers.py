from tikapy import TikapyClient
from tikapy import TikapySslClient

class IPsecPeers:
    def __init__(self,address,username,password):
        self.client = TikapyClient( address, 8728 )
        self.client.login( username,password)

    def listPeers(self):
        """
        Method will list peers
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/peer/print'])
        print("Address\tPort\tProposal\tHash\tEncryption")
        for i in ipsec:
            print(ipsec[i]['address']+"\t"+ipsec[i]['port']+"\t"+ipsec[i]['proposal-check']+"\t"+ipsec[i]['hash-algorithm']+"\t"+ipsec[i]['enc-algorithm'])
        return ipsec

    def addPeer(self):
        """
        Method will add peer
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/peer/add'])
        return ipsec

    def removePeer(self,number):
        """
        Method will remove peer
        :param number:
        :return:
        """
        ipsec = self.client.talk(['/ip/ipsec/peer/remove','=numbers='+number])
        return ipsec

    def enablePeer(self,number):
        """
        Method will enable peer
        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/enable', '=numbers=' + number] )
        return ipsec

    def disablePeer(self,number):
        """

        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/disable', '=numbers=' + number] )
        return ipsec

    def commentPeer(self,number,comment):
        """
        Method will comment peer
        :param number:
        :param comment:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/comment', '=numbers=' + number,'=comment='+comment] )
        return ipsec

    def setAddress(self,number,address):
        """
        Method will se taddress
        :param number:
        :param address:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=address=' + address] )
        return ipsec

    def setPort(self,number,port="500"):
        """
        Method will set port
        :param number:
        :param port:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=port=' + port] )
        return ipsec

    def setLocalAddress(self,number,laddress):
        """
        Method will set local address
        :param number:
        :param laddress: LAN address
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=local-address=' + laddress] )
        return ipsec

    def setAuthMethod(self,number,method="pre-shared-key"):
        """

        :param number:
        :param method: pre-shared-key,pre-shared-key-xauth,rsa-key,rsa-signature,rsa-signature-hybrid
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=auth-method=' + method] )
        return ipsec

    def setPassive(self,number):
        """
        Method will set passive method
        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=passive=yes'] )
        return ipsec

    def setSecret(self,number,password):
        """
        Method will set tunnel secret
        :param number:
        :param password:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=secret=' + password] )
        return ipsec

    def setPolicyTemplateGroup(self,number, tmp="default"):
        """
        Method will set policy template
        :param number:
        :param tmp:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=policy-template-group=' + tmp] )
        return ipsec

    def setExchangeMethod(self,number,method="main"):
        """
        methdd will set method
        :param number:
        :param method: aggressive, base,main,main-l2tp
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=exchange-mode=' + method] )
        return ipsec

    def sendInitialCOntact(self,number):
        """

        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=send-initial-contact=yes'] )
        return ipsec

    def natTraversal(self,number):
        """

        :param number:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=nat-traversal=yes'] )
        return ipsec

    def setId(self,number,username=None):
        """
        Method will set username
        :param number:
        :param username: auto, fqdn:username,user-fqdn:username
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=my-id=' + username] )
        return ipsec

    def setProposalCheck(self,number,proposal="obey"):
        """
        Method will set proposal check
        :param number:
        :param proposal: claim, exact, obey, strict
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=proposal-check=' + proposal] )
        return ipsec

    def setHashAlgorithm(self,number,alg="sha1"):
        """
        Method will set hashing alghoritm
        :param number:
        :param alg: md5, sha1,sha256,sha512
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=hash-algorithm=' + alg] )
        return ipsec

    def setEncryptionAlgorithm(self,number,alg="3des,aes-128"):
        """
        Method will se tencryption
        :param number:
        :param alg: 3des,aes-128,aes-192,aes-256,blowfish,camelia-128,camelia-192,camelia-256,des
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=enc-algorithm=' + alg] )
        return ipsec

    def setModeConfiguration(self,number,mode="request-only"):
        """
        Method will set mode
        :param number:
        :param mode: request-only or cfg file
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=mode-config=' + mode] )
        return ipsec

    def setDhGroup(self,number,dh="modp1024"):
        """
        Method will set modp
        :param number:
        :param dh: modp768,modp1024,ec2n155,ec2n185,modp1536,modp2048,modp3072,modp4096,modp6144,modp8192
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=dh-group=' + dh] )
        return ipsec

    def generatePolicy(self,number,policy="no"):
        """
        Method will generate policy
        :param number:
        :param policy: no,port-override,port-strict
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=generate-policy=' + policy] )
        return ipsec

    def setLifetime(self,number,life="1d 00:00:00"):
        """
        Method will set lifetime
        :param number:
        :param life:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=lifetime=' + life] )
        return ipsec

    def setLifeBytes(self,number,bytes="0"):
        """
        Method will se t lifetime byes
        :param number:
        :param bytes:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=lifebytes=' + bytes] )
        return ipsec

    def setDpdInterval(self,number,interval="120"):
        """
        Methgod will set dpd interval
        :param number:
        :param interval: interval to check in secs
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=dpd-interval=' + interval] )
        return ipsec

    def setDpdMaxFailures(self,number,maximum="5"):
        """
        Method will set max failures for dpd
        :param number:
        :param maximum:
        :return:
        """
        ipsec = self.client.talk( ['/ip/ipsec/peer/set', '=numbers=' + number, '=dpd-maximum-failures=' + maximum] )
        return ipsec