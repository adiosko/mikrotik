from tikapy import TikapyClient
from tikapy import TikapySslClient

class BwTest:
    def __init__(self,address,username,password):
        self.client = TikapySslClient( address, 8729 )
        self.client.login( username,password)

    def  setTcpBwTest(self,testTo,direction,TcpConnectionCount,username,password,duration):
        """
        Method will test TCP bandwidth
        :param testTo: IP address of destination server
        :param direction: both/receive/send
        :param TcpConnectionCount: 20 default
        :param duration: duration of test
        :return: list
        """
        bwt = self.client.talk(['/tool/bandwidth-test','=address='+testTo,'=protocol=tcp','=direction='+direction,
                                '=tcp-connection-count='+TcpConnectionCount,'=user='+username,'=password='+password
                                ,'=duration='+duration])
        return bwt

    def setUdpBwTest(self,testTo,LocalTx,RemoteTx,direction,username,password,duration):
        """
        Method will test UDP bw test
        :param testTo: IP of remote server
        :param LocalTx: default 1500
        :param RemoteTx: def 1500
        :param direction: both/receive/send
        :param username: username of device
        :param password: password of device
        :param duration: length of test
        :return:
        """
        bwt = self.client.talk(['/tool/bandwidth-test','=address='+testTo,'=protocol=udp','=local-tx-speed='+LocalTx,
                                '=remote-tx-speed='+RemoteTx,'=direction='+direction,'=user='+username,
                                '=password='+password,'=duration='+duration])
        print(bwt)
        return bwt