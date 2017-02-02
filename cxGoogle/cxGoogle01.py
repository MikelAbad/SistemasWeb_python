# coding: UTF-8

import httplib #Librería HTTP

print "\r\n---> Estableciendo conexión TCP"
servidor = 'www.google.com' #Definir servidor
conn = httplib.HTTPConnection(servidor) #Definir conexion
# Alternativa sin definir servidor:  conn = httplib.HTTPConnection('www.google.com', '80')
conn.connect() #Establece conexión
print "---> Conexión TCP establecida"

print  conn.sock.getsockname() #Imprimir dupla
print " Local IP address is " + str(conn.sock.getsockname()[0]) #str = toString
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

conn.close() # Cerrar conexión
