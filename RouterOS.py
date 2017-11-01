import  tikapy
import sys
import six

api = tikapy.TikapyClient(address="e4:8d:8c:12:49:64",port="8728")
api.login(user="admin",password='""')
api.talk("/interface/print")
api.talk("/ip/address/print")
api.disconnect()