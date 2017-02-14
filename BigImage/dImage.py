import httplib

print "\r\n---> Estableciendo conexion TCP..."
server = 'www.httpwatch.com'
conn = httplib.HTTPConnection(server)
conn.connect()
print "---> Conexion TCP establecida"

conn.sock.getsockname()
print "\r\n Local IP address is " + str(conn.sock.getsockname()[0])
print " Local TCP port is " + str(conn.sock.getsockname()[1])
print "\r\n---> Configurando parametros de la peticion HTTP"

metod = 'GET'
uri = '/httpgallery/chunked/chunkedimage.aspx'
headers = {'Host': server,
           'User-Agent': 'Cliente Python',
            }
bodyP = ''

conn.request(metod, uri, headers=headers, body=bodyP)
print "\r\n---> Realizando peticion HTTP..."

print "---> Recibiendo respuesta HTTP..."
response = conn.getresponse()
print "\r\n STATUS: " + str(response.status) + "    " + str(response.reason)
bodyR = response.read()

f = open('imagenTrozos.jpg', 'wb')
f.write(bodyR)
f.close()

conn.close()