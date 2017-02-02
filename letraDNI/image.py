# coding: UTF-8

import httplib
import urllib

servidor = 'websystems-2.appspot.com'
conn = httplib.HTTPConnection(servidor)
conn.connect()

param = {'image': "websystems&kungfu"}
param_encoded = urllib.urlencode(param)

uri = '/' + '?' + param_encoded
print uri

headers = {'Host': servidor,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()
print 'STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

location = respuesta.getheader('location')
print " Location: " + location

array = location.split('/')
uri = '/' + array[3]
print 'Nueva uri: ' + uri

print 'servidor = ' + servidor
conn = httplib.HTTPConnection(servidor)
conn.connect()

conn.request('GET', uri, headers = headers, body=cuerpo_peticion)
respuesta=conn.getresponse()
print 'STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

location = respuesta.getheader('location')
print " Location: " + location

f = open('kungfu.jpg','wb')
f.write(urllib.urlopen(location).read())
f.close()


conn.close()