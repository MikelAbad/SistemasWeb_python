# coding: UTF-8

import httplib
import urllib

servidor = 'tic-investigacion-1.appspot.com'
conn = httplib.HTTPConnection(servidor)
conn.connect()

uri = '/processForm'
param = {'nan': '74839218'}

param_encoded = urllib.urlencode(param)
headers = {'Host': servidor,
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': str(len(param_encoded))}

conn.request('POST',uri,headers = headers,body=param_encoded)
respuesta=conn.getresponse()
print 'STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)
print 'CONTENT: ' + respuesta.read()

conn.close()