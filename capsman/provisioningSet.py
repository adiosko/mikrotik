from tikapy import TikapyClient
from tikapy import TikapySslClient

class provisioningSet:
    def __init__(self, address, username, password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login(username, password)

    def setRadioMac(self,number,mac="00:00:00:00:00:00"):
        """

        :param number:
        :param mac:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set','=numbers='+number,'=radio-mac='+mac])
        return wifi

    def setHwSupportedModels(self,number,model="a"):
        """

        :param number:
        :param model:  a,a-turbo,ac,an,b,g,g-turbo,gn
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=hw-supported-modes=' + model])
        return wifi

    def setIdentityRegexp(self,number,regexp):
        """

        :param number:
        :param regexp:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=identity-regexp=' + regexp])
        return wifi

    def setCommonNameRegexp(self,number,regexp):
        """

        :param number:
        :param regexp:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=common-name-regexp=' + regexp])
        return wifi

    def setIpRanges(self,number,ipFrom,ipTo):
        """

        :param number:
        :param ipFrom:
        :param ipTo:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=ip-address-ranges=' + ipFrom+"-"+ipTo])
        return wifi

    def setAction(self,number,action="create-dynamic-enabled"):
        """

        :param number:
        :param action: create-dynamic-enabled,create-enabled,create-disabled,none
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=action=' + action])
        return wifi

    def setMasterCOnfiguration(self,number,configName):
        """

        :param number:
        :param configName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=master-configuration=' + configName])
        return wifi

    def setSlaveConfiguration(self,number,configName):
        """

        :param number:
        :param configName:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=slave-configurations=' + configName])
        return wifi

    def setNameFormat(self,number,format="prefix"):
        """

        :param number:
        :param format: prefix,cap,identity,prefix-identity
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '=numbers=' + number, '=name-format=' + format])
        return wifi

    def setNamePrefix(self,number,prefix):
        """

        :param number:
        :param prefix:
        :return:
        """
        wifi = self.client.talk(['/caps-man/provisioning/set', '-numbers=' + number, '=name-prefix=' + prefix])
        return wifi