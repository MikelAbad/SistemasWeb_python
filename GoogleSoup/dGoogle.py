import httplib
from bs4 import BeautifulSoup

print " Conectando con Google..."
servidor = 'www.google.es'
conn = httplib.HTTPConnection(servidor)
conn.connect()
print " Conectado."

print " Local IP address: " + str(conn.sock.getsockname()[0])
print " Local TCP port: " + str(conn.sock.getsockname()[1])

metodo = 'GET'
recurso = '/'
cabeceras_peticion = {'Host': servidor,
                      'User-Agent': 'Cliente Python'}
cuerpo_peticion = ''
conn.request(metodo, recurso, headers=cabeceras_peticion, body=cuerpo_peticion)

response = conn.getresponse()
print " STATUS: " + str(response.status)
print " STATUS DESCRIPTION: " + str(response.reason)

if response.status == 200:
    webContent = response.read()
    html = BeautifulSoup(webContent, "html.parser")

    print "\n/////// HTML HEAD:"
    print html.head
    print "/////// HTML HEAD NAME:"
    print html.head.name
    print "/////// HTML HEAD STRING:"
    print html.head.string
    print "/////// HTML HEAD META CONTENT:"
    print html.head.meta['content']
    print "/////// HTML TITLE:"
    print html.title
    print "/////// HTML TITLE STRING:"
    print html.title.string
    print "/////// HTML P:"
    print html.p
    print "/////// HTML P NAME:"
    print html.p.name
    print "/////// HTML P STRING:"
    print html.p.string
    print "/////// HTML P STYLE"
    print html.p['style']
    print "/////// HTML P GET STYLE"
    print html.p.get('style')
    print "/////// HTML P TEXT"
    print html.p.text
    print "/////// HTML P A"
    print html.p.a
    print "/////// HTML P A STRING"
    print html.p.a.string
    print "/////// HTML A"
    print html.a
    print "/////// HTML P A PARENT NAME"
    print html.p.a.parent.name
    print "/////// HTML A PARENT NAME"
    print html.a.parent.name
    print "/////// HTML P A"
    print html.p.a
    print "/////// HTML A"
    print html.a

    print "\n/////// Todos los enlaces"
    for enlace in html.find_all('a'):
        print enlace

    print "\n/////// Todos los textos"
    print(html.get_text())


conn.close()