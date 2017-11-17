#toto je testovacie prostredie na testovanie kodu

from tikapy import TikapyClient
from pprint import pprint
import tikapy
import os

client =  TikapyClient('172.16.129.2',8728)

client.talk(['/system/package/update/check-for-updates'])
#os.system("sshpass -p 'admin' scp /home/adrian/Desktop/ExtendVolume  admin@172.16.129.2:volume1")
#os.system("sshpass -p 'admin' scp admin@172.16.129.2:backup.backup /home/adrian/Desktop/router")

'''
client.login('admin','admin')
#pprint(client.__setattr__(name="meno", passw="password"))
#pprint(client.talk(['/ip/address/print']))
#pprint(client.talk(['/user/add/'])

#def add_user(name, password, disabled=False, group=write):
pprint(client.talk(['/file/print']))

#add_user("test", ""))
client.disconnect()
'''



'''
import pexpect
import os

#os.system("mactelnet e4:8d:8c:12:49:64 -u admin -p admin")
child = pexpect.spawn("mactelnet e4:8d:8c:12:49:64")
child.expect("Username: ")
child.sendline("admin+t")
child.expect("Password: ")
child.sendline("admin")
child.send("\r")
child.expect('> ')
child.sendline('/interface/print')
child.expect('> ')
child.close()
'''