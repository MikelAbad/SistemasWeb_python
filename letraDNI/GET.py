# coding: UTF-8

import httplib
import urllib

servidor = 'tic-investigacion-1.appspot.com'
conn = httplib.HTTPConnection(servidor)
conn.connect()

param = {'nan': '74839218'}
param_encoded = urllib.urlencode(param)

uri = '/processForm' + '?' + param_encoded
print uri

headers = {'Host': servidor,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()
print 'STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)
print 'CONTENT: ' + respuesta.read()

conn.close()