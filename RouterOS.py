#toto je testovacie prostredie na testovanie kodu
#nepodpora api
from tikapy import TikapyClient
from pprint import pprint
import tikapy
import os

client = TikapyClient('172.16.129.2', 8728)
client.login('admin','admin')

print(client.talk( ['/certificate/create-certificate-request', '=template=cert1', '= key-passphrase=pass']))


client.disconnect()