# coding: UTF-8

import httplib

print "\r\n---> Estableciendo conexión TCP"
servidor = 'www.google.com'
conn = httplib.HTTPConnection(servidor)
conn.connect()
print "---> Conexión TCP establecida"

print " Local IP address is " + str(conn.sock.getsockname()[0])
print " Local TCP port is " + str(conn.sock.getsockname()[1])

print "---> Configurando parámetros de la petición HTTP"
metodo = 'GET'
recurso = '/'
cabeceras_peticion = {'Host': servidor,
                      'User-Agent': 'Cliente Python'}
cuerpo_peticion = ''
print "---> Realizando petición HTTP"
conn.request(metodo, recurso, headers=cabeceras_peticion, body=cuerpo_peticion)

print "---> Recibiendo respuesta HTTP"
response = conn.getresponse()
print " STATUS: " + str(response.status)
print " STATUS DESCCRIPTION: " + str(response.reason)

location = response.getheader('location')
print " Location: " + location

array = location.split('/')
print 'Nueva direccion: ' + array[2]

conn.close()

print '\r\n'
print 'REDIRECCION'
print '\r\n'

print "---> Estableciendo conexión TCP"
servidor = str(array[2])
conn = httplib.HTTPConnection(servidor)
conn.connect()
print "---> Conexión TCP establecida"

print " Local IP address is " + str(conn.sock.getsockname()[0])
print " Local TCP port is " + str(conn.sock.getsockname()[1])

print "---> Configurando parámetros de la petición HTTP"
metodo = 'GET'
recurso = '/' + str(array[3])
cabeceras_peticion = {'Host': servidor,
                      'User-Agent': 'Cliente Python'}
cuerpo_peticion = ''
print "---> Realizando petición HTTP"
conn.request(metodo, recurso, headers=cabeceras_peticion, body=cuerpo_peticion)

print "---> Recibiendo respuesta HTTP"
response = conn.getresponse()
print " STATUS: " + str(response.status)
print " STATUS DESCCRIPTION: " + str(response.reason)

webContent = response.read()

f = open('googlePrueba.html', 'w')
f.write(webContent)
f.close()

conn.close()
