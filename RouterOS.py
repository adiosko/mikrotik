#toto je testovacie prostredie na testovanie kodu

from tikapy import TikapyClient
from pprint import pprint
import tikapy

client =  TikapyClient('192.168.1.1',8728)

client.login('admin','admin')
#pprint(client.__setattr__(name="meno", passw="password"))
#pprint(client.talk(['/ip/address/print']))
#pprint(client.talk(['/user/add/'])

#def add_user(name, password, disabled=False, group=write):
client.talk(['/user/set','=numbers=adrian','=group=read'])

#add_user("test", ""))
client.disconnect()



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