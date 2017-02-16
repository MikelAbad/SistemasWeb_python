def print_response_headers(respuesta):
    cabeceras = respuesta.getheaders()
    for each in cabeceras:
        if cabeceras.index(each) == 0:
            print "     HEADERS: " + each[0] + ":" + each[1]
        else:
            print "     " + each[0] + each[1]