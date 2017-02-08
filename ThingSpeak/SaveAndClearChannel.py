import psutil
import httplib
import urllib

server = 'api.thingspeak.com'
conn = httplib.HTTPConnection(server)
conn.connect()

param = {'api_key': 'DBW8693HSEU16SHT',
         'metadata': True,}
param_encoded = urllib.urlencode(param)

uri = '/channels/224662/feeds?' + param_encoded

headers = {'Host': server,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
response=conn.getresponse()
print 'STATUS:  ' + str(response.status) + '   ' + str(response.reason)

f = open('datos.txt','w')
f.write(response.read())
f.close()

conn.close()

 #DELETE FEED

servidor = 'api.thingspeak.com'
conexion = httplib.HTTPConnection(servidor)
conexion.connect()

uri = '/channels/224662/feeds'
parametro = {'api_key': '7ZEVD4MVX39VS4X6',}
parametro_encoded = urllib.urlencode(parametro)
cabeceras = {'Host': servidor,}

conexion.request('DELETE',uri,headers = cabeceras,body=parametro_encoded)
respuesta=conexion.getresponse()
print 'STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

location = respuesta.getheader('location')
print " Location: " + location

conexion.close()