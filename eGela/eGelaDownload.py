import httplib
import urllib

us = 'user'
pw = 'pass'

# Realizamos una primera conexion a eGela
servidor = 'egela.ehu.es'
conn = httplib.HTTPConnection(servidor)
conn.connect()

uri = '/'

headers = {'Host': servidor,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()

print '\nPrimera conexion:'
print ' STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

location = respuesta.getheader('location')
print "  Location: " + location

array = location.split('/')

conn.close()

# Redireccionamos segun la location

servidor = array[2]
conn = httplib.HTTPSConnection(servidor)
conn.connect()

uri = '/'

headers = {'Host': servidor,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()

print '\n Redireccion:'
print '  STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

conn.close()

# Cogemos la Cookie y pedimos de nuevo

conn = httplib.HTTPSConnection(servidor)
conn.connect()

uri = '/login/index.php'

setcookie = respuesta.getheader('set-cookie').split(';')
cookie = setcookie[0]

headers = {'Host': servidor,
           'Cookie': cookie,}
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta = conn.getresponse()

print '\n Conexion con Cookie:'
print '  STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

conn.close()

# Pasamos a conectarnos con los datos

conn.connect()

param = {'username': us,
         'password': pw,}

param_encoded = urllib.urlencode(param)
headers = {'Host': servidor,
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': str(len(param_encoded)),
           'Cookie': cookie,
           }

conn.request('POST',uri,headers = headers,body=param_encoded)
respuesta=conn.getresponse()

print "\n Realizando login:"
print '  STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

location = respuesta.getheader('location')
print "   Location: " + location

conn.close()

#Siguiente conexion con la nueva Cookie

conn.connect()

setcookie = respuesta.getheader('set-cookie').split(';')
cookie = setcookie[0]

array = location.split('/')
uri = '/' + array[4]

headers = {'Host': servidor,
           'Cookie': cookie,
           }
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()

print '\n Estableciendo conexion:'
print '  STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

conn.close()

# Entramos en la pagina de Sistemas Web

conn.connect()

uri = '/course/view.php?id=6975'

headers = {'Host': servidor,
           'Cookie': cookie,
           }
cuerpo_peticion = ''

conn.request('GET',uri,headers = headers,body=cuerpo_peticion)
respuesta=conn.getresponse()

print '\n Entrando a Sistemas Web:'
print '  STATUS:  ' + str(respuesta.status) + '   ' + str(respuesta.reason)

print '\n Guardando Sistemas Web...'
webContent = respuesta.read()

f = open('eGelaSistemasWeb.html', 'w')
f.write(webContent)
f.close()

print '\n Pagina Sistemas Web de eGela descagada con exito'

conn.close()