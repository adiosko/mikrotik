from tikapy import TikapyClient
from tikapy import TikapySslClient

class TrafficGenerator:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def setTrafficId(self,ID):
        """
        Method will set traffic id
        :param ID: number
        :return:
        """
        traff = self.client.talk(['/tool/traffic-generator/set','=test-id='+ID])
        return traff

    def setLatency(self,latency):
        """
        Method will set latency
        :param latency: in mikrosecs
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/set', '=latency-distribution-max=' + latency] )
        return traff

    def setSamplesToKeep(self,samples):
        """
        Method will set max samples to keep
        :param samples:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/set', '=stats-samples-to-keep=' + samples] )
        return traff

    def setquickStartId(self,id,stream):
        """
        method will set quick start test id
        :param id:
        :param stream: steram to set
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=test-id=' + id,'=stream='+stream] )
        return traff

    def setquickPort(self,stream,port):
        """
        Method will set  steram and port
        :param stream:
        :param port:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=port='+port] )
        return traff

    def setquicInterface(self,stream,interface):
        """
        Method will set interface to use
        :param stream:
        :param interface:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=interface='+interface] )
        return traff

    def setQuickPacketSize(self,stream,packetSize):
        """
        Method will set pakcet size of stream
        :param stream:
        :param packetSize:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=packet-size='+packetSize] )
        return traff

    def setQuickPPS(self,stream,PPS):
        """
        Method will set stream PPS
        :param stream:
        :param PPS:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=pps='+PPS] )
        return traff

    def setQuickMBPS(self,stream,mbps):
        """
        Method will set stream mbps
        :param stream:
        :param mbps:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=mbps='+mbps] )
        return traff

    def setQuickTxTemplate(self,stream,template):
        """
        Method will set tx template for stream
        :param stream:
        :param template:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/quick', '=stream=' + stream,'=tx-template='+template] )
        return traff

    def startGenerator(self):
        """
        Method will start generator
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/start'] )
        return traff

    def stopGenerator(self):
        """
        Method will stop generator
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stop'] )
        return traff

    def injectPcapInterface(self,interface):
        """
        Method will set pcap iface
        :param interface:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/inject','=interface='+interface] )
        return traff

    def injectPcapFile(self,interface,file):
        """
        Method will inject pcap file
        :param interface:
        :param file:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/inject','=data='+file,'=interface='+interface] )
        return traff

    def listStreamStats(self):
        """
        Method will list stream stats
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stats/stream/print'] )
        return traff

    def listLatencyDists(self):
        """
        Method will list latency distributions
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stats/latency-distribution/print'] )
        if traff == {}:
            print("No latency found")
        else:
            print("Latency\tCount\tShare")
            for i in traff:
                print(traff[i]['latency']+"\t"+traff[i]['count']+"\t"+traff[i]['share'])
        return traff

    def listPorts(self):
        """
        Method will list ports on generator
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stats/port/print'] )
        return traff

    def listRaws(self):
        """
        Method will list all raws for generator
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stats/raw/print'] )
        return traff

    def listGeneratorPorts(self):
        """
        Method will list all generator ports
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/print'] )
        if traff == {}:
            print("No port found")
        else:
            print("Name\tinterface\tfirst header")
            for i in traff:
                print(traff[i]['name']+"\t"+traff[i]['interface']+"\t"+traff[i]['first-header'])
        return traff

    def addGeneratorPort(self,interface):
        """
        Method will add interface to generator
        :param interface:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/add','=interface='+interface] )
        return traff

    def setNamePort(self,oldname,newname):
        """
        Method will set port name
        :param oldname: old name of port
        :param newname: new name of port
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/set','=numbers='+oldname,'=name='+newname] )
        return traff

    def setInterfacePort(self,name,interface):
        """
        Method will set interface name
        :param name:
        :param interface:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/set', '=numbers=' + name, '=interface=' + interface] )
        return traff

    def setFirstHeader(self,name,header):
        """
        Method will set first header of name
        :param name:
        :param header: always mac
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/set', '=numbers=' + name, '=name=' + header] )
        return traff

    def enableGeneratorPort(self,name):
        """
        Method will enablegenerator port
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/set', '=numbers=' + name, '=disabled=no'] )
        return traff

    def disableGeneratorPort(self,name):
        """
        Method will disable generatoir port
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/set', '=numbers=' + name, '=disabled=yes'] )
        return traff

    def removeGeneratorPort(self,name):
        """
        Method will remove generator port
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/port/remove', '=numbers=' + name] )
        return traff

    def addPacketTemplate(self,name):
        """
        Method will add new packet template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/add', '=name=' + name] )
        return traff

    def setPacketTemplateHeader(self,name,header):
        """
        Method will set header of template
        :param name:
        :param header: ip, ipv6, raw, tcp, udp, vlan
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/set', '=numbers=' + name,'=header-stack='+header] )
        return traff

    def setPacketTemplateData(self,name,data):
        """
        Method will set name template data
        :param name:
        :param data: incrementing, random, specific-byte, uninitialized
        :return:
        """
        traff = self.client.talk(['/tool/traffic-generator/packet-template/set', '=numbers=' + name,
                                  '=data=' + data] )
        return traff

    def setPacketTemplatePort(self,name,port):
        """
        Method will set template port
        :param name:
        :param port:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/set', '=numbers=' + name,
                                   '=port=' + port] )

        return traff

    def setPacketTemplateInterface(self,name,interface):
        """
        Method will set template interface
        :param name:
        :param interface:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/set', '=numbers=' + name,
                                   '=interface=' + interface] )

        return traff

    def removePAcketTemplate(self,name):
        """
        Method will remove packet template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/remove', '=numbers=' + name])
        return traff

    def commentPacketTemplate(self,name,comment):
        """
        Method will comment template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/packet-template/set', '=numbers=' + name,
                           '=comment=' + comment] )
        return traff

    def listRawPacketTemplates(self):
        """
        Method will list raw packet templates
        :return:
        """
        traff = self.client.talk(['/tool/traffic-generator/raw-packet-template/print'])
        if traff == {}:
            print("No raw template found")
        else:
            print("Name\theader\theader length\tip header offset")
            for i in traff:
                print(traff[i]['name']+"\t"+traff[i]['header']+"\t"+traff[i]['header-length']+"\t"
                      +traff[i]['ip-header-offset'])
        return traff

    def addRawPacketTemplate(self,name):
        """
        Method will add raw templatew
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/add','=name='+name] )
        return traff

    def setRawHeader(self,name,header):
        """
        Method will set header of file
        :param name:
        :param header:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=header='+header] )
        return traff

    def setRawPort(self,name,port):
        """
        Method will set port of raw template
        :param name:
        :param port:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=port='+port] )
        return traff

    def setRawData(self,name,data):
        """
        Method will set raw data
        :param name:
        :param data: incremeneting, random, specific-type, uninitialized
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=data='] )
        return traff

    def setIPHeaderOffsetRaw(self,name,offset):
        """
        Method will set offset
        :param name:
        :param offset:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=ip-header-offset='+offset] )
        return traff

    def setIpv6HeaderOffset(self,name,offset):
        """
        Method will set Ipv6 offset
        :param name:
        :param offset:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=ipv6-header-offset='+offset] )
        return traff

    def setUdpHeaderOffset(self,name,offset):
        """
        Method will set udp level offset
        :param name:
        :param offset:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=udp-header-offset=' + offset] )

        return traff

    def useSpecialFooter(self,name):
        """
        Method will set special foot
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=special-footer=yes'] )

        return traff

    def dontUseSpecialFooter(self,name):
        """
        Method will dont use special footer
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=special-footer=no'] )

        return traff

    def removeRawTemplate(self,name):
        """
        Method will remove raw template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/remove', '=numbers=' + name] )

        return traff

    def commentRawTemplate(self,name,comment):
        """
        Method will comment raw template
        :param name:
        :param comment:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/raw-packet-template/set', '=numbers=' + name,
                                   '=comment='+comment] )

        return traff

    def listStreams(self):
        """
        Method will list all streams
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stream/print'] )
        if traff == {}:
            print("no stream found")
        else:
            print("Name\tID\tpakcet size\ttx template")
            for i in traff:
                print(traff[i]['name']+"\t"+traff[i]['id']+"\t"+traff[i]['packet-size']+"\t"+traff[i]['tx-template'])
        print(traff)
        return traff

    def addStream(self,name,template):
        """
        Method will add stream
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stream/add','=name='+name,'=tx-template='+template] )
        return traff

    def removeStreamTemplate(self,name):
        """
        Method will remove stream template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stream/remove','=numbers='+name] )
        return traff

    def enableStreamTemplate(self,name):
        """
        Method will enable template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stream/enable','=numbers='+name] )
        return traff

    def disableStreamTemplate(self,name):
        """
        Method will disable template
        :param name:
        :return:
        """
        traff = self.client.talk( ['/tool/traffic-generator/stream/disable','=numbers='+name] )
        return traff