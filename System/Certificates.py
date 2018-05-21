from tikapy import TikapyClient
from tikapy import TikapySslClient

class Certificates:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def listCertificates(self):
        certs = {}
        if self.client.talk(['/certificate/print']) == {}:
            print("There are no certificates imported or created on mikrotik")
        else:
            certs = self.client.talk(['/certificate/print'])
            print("Name\tCommon-name\tkey-usage\tkey-size\tcrlusage")
            for i in certs:
                print(certs[i]['name']+" "+certs[i]['common-name']+" "+certs[i]['key-usage']+" "+certs[i]['key-size']
                +" "+certs[i]['crl'])
        return certs

    def useCRL(self):
        """
        Method will allow certificate crl file to download
        :return:  dictionary of certs
        """
        certs = self.client.talk(['/certificate/settings/set','=crl-download=yes','=crl-use=yes'])
        return certs

    def notUseCRL(self):
        """
        Method will deny crl download
        :return: dictionary of words
        """
        certs = self.client.talk(['/certificate/settings/set','=crl-download=no','=crl-use=no'])
        return certs

    def addCertificate(self,name,commonName,trusted,country):
        """
        Generate standard certificate crt on mikrotik
        :param name: name of your certificate
        :param commonName:  common name of certificate
        :param trusted: trusted status yes or no
        :param country: 2 letter country code
        :return: dictionary of certs
        """
        cert = self.client.talk(['/certificate/add','=name='+name,'=common-name='+commonName,'=trusted='+trusted,'=country='+country])
        return cert

    def setCertificateLocality(self,certName,locality):
        """
        Method will setup certification locality (city)
        :param certName: name of certificate
        :param locality: city
        :return: list of words
        """
        certs = self.client.talk(['/certificate/set','=numbers='+certName,'=locality='+locality])
        return certs

    def setCertificateState(self,certName,state):
        """
        Method will setup certificate State
        :param certName: name of certificate
        :param state: state of certificate
        :return: list of words
        """
        certs = self.client.talk(['/certificate/set','=numbers='+certName,'=state='+state])
        return certs

    def setCertificateOrg(self,certName,organisation):
        """
        Method will setup certificate organization group
        :param certName: certname
        :param organisation:  organization name
        :return: list of words
        """
        cert = self.client.talk(['/certificate/set','=organization='+organisation])
        return cert

    def setAlternateNameMethod(self,certName,subject):
        """
        Method will setup ertificate for IP/DNS/email in format f.e: mail:test@test
        :param certName: name of certificate
        :param subject: IP/DNS/mail:
        :return: list of words
        """
        cert = self.client.talk(['/certificate/set','=numbers='+certName,'=subject-alt-name='+subject])
        return cert

    def setCertificateKeySize(self,certName,keySize):
        """
        Method will setup key size of cert
        :param certName: name of cert
        :param keySize: in string 1024,1536,2048,4096,8192
        :return:list of words
        """
        certs = self.client.talk(['/certificate/set','=numbers='+certName,'=key-size='+keySize])
        return certs

    def setCertificateValidation(self,certName,ValidateFor):
        """
        Method will setup validation time of certificate on mt
        :param certName: cert name
        :param ValidateFor:  time in days in string
        :return: list of words
        """
        certs = self.client.talk(['/certificate/set','=numbers='+certName,'=days-valid='+ValidateFor])
        return certs

    def setKeyUsage(self,certName,Keys):
        """
        Method will setup keys for certificate usage
        Words are:
        digital-signature, content-commitment, key-encipherment, code-sign, crl-sign, data-encipherment, decipher-only,
        dvcs,email-protect,encipher-only,ipsec-end-system,ipsec-tunnel,ipsec-user,key-agreement,key-cert-sign,
        oscp-sign,server-gated-crypto,timestamp,tls-client,tls-server
        :param certName: name of cert
        :param Keys: keys included in emthod description
        :return: list of words
        """
        certs = self.client.talk(['/certificate/set','=numbers='+certName,'=key-usage='+Keys])
        return certs

    def removeCertificate(self,certName):
        """
        Method will remove certificate by its name
        :param certName: cert name yu want to delete
        :return: list of words
        """
        certs = self.client.talk(['/certificate/remove','=numbers='+certName])
        return certs

    def importCertificate(self,certName,Password):
        certs = self.client.talk(['/certificate/import','=file-name='+certName,'=passphrase='+Password])
        return  certs
    #opravit
    def reinstallSMartCard(self,PIN):
        certs = self.client.talk(['/certificate/card-reinstall', '=pin='+PIN])
        print(certs)
        return certs
    #opravit
    def verifyCard(self,PIN=1234):
        certs = self.client.talk( ['/certificate/card-verify', '=pin=' + PIN])
        print(certs)
        return certs
    #opravit

    def revokeCertificate(self,certName):
        certs = self.client.talk(['/certificate/issued-revoke','=numbers='+certName])
        print(certs)
        return certs

    def createCertificateRequest(self,certName,passphrase):
        certs = self.client.talk(['/certificate/create-certificate-request','=template='+certName,'= key-passphrase='+passphrase])
        return certs

    def listSCEPServers(self):
        certs = self.client.talk(['/certificate/scep-server/print'])
        if certs == {}:
            print("No SCEP servers found")
        else:
            print(certs)
        return certs

    #otazka ci implementovat
    def addSCEPServer(self,ca,pathToCA,valid,lifetime):
        certs = self.client.talk(['/certificate/scep-server/add','=ca-cert='+ca
                                  ,'=path='+pathToCA,'=days-valid='+valid
                                  ,'=request-lifetime='+lifetime])
        return certs


    def listRaProxy(self):
        """
        Method will list all proxy connected to scep server
        :return:  list of words
        """
        certs = self.client.talk(['/certificate/scep-server/ra/print'])
        if certs == {}:
            print("There are no proxy setup")
        else:
            print(certs)
        return certs

    def  generateOTPPassword(self,minutes):
        """
        Method will generate passwords for certificates
        :param minutes: count of minutes to use
        :return: list of certs
        """
        certs = self.client.talk(['/certificate/scep-server/otp/generate','=minutes-valid='+minutes])
        return certs

    def listOTPPasswords(self):
        """
        Method will list generated passwords for certs
        :return: list of passwords (hash)
        """
        certs = self.client.talk(['/certificate/scep-server/otp/print'])
        if certs == {}:
            print("No passwords generated")
        else:
            print("Password\texpiresIn\tUsed")
            for i in certs:
                print(certs[i]['password']+" "+certs[i]['expires']+" "+certs[i]['used'])
        return  certs