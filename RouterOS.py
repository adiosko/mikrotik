#toto je testovacie prostredie na testovanie kodu

from tikapy import TikapyClient
from pprint import pprint

client =  TikapyClient('172.16.49.2',8728)

client.login('admin','admin')
pprint(client.talk(['/interface/print']))
pprint(client.talk(['/ip/address/print']))
pprint(client.talk(['/ip/route/print']))

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