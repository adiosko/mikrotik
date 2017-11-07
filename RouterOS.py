#api = tikapy.TikapyClient()
import os
import tikapy
import pprint
import socket
import librouteros
import rosapi

#os.system("echo -e '9305148094' | sudo macping e4:8d:8c:12:49:64 -c 4")

#api = tikapy.TikapyClient("Adventura", 8728)
#password = ''
#api.login( "admin", "'")
#api.talk(['/interface/print'])
#api.talk(['/interfaces/print'])
#api.talk(['/ip/address/print'])
#pprint(api.talk(['/ip/address/print']))
#api.disconnect()
#socket = socket.create_connection("e4:8d:8c:12:49:64")
sock = socket.create_connection(("74:D4:35:E6:8D:0D",8291))
api1 = librouteros.connect(username="admin",password="admin",socker=sock)





