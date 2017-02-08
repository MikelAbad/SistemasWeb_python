import psutil
import httplib
import urllib

while True:
    print "\r\n Gathering information, wait 15 seconds please..."
    cpuPercent = psutil.cpu_percent(interval=15)
    ramPercent = psutil.virtual_memory().percent
    print "\r\n CPU = " + str(cpuPercent) + "   RAM = " + str(ramPercent)

    server = 'api.thingspeak.com'
    conn = httplib.HTTPConnection(server)
    conn.connect()

    uri = '/update'
    params = {'api_key': 'LSTXG45LYRYPQD41',
              'field1': str(cpuPercent),
              'field2': str(ramPercent),
              }

    param_encoded = urllib.urlencode(params)
    headers = {'Host': server,
               'Content-Length': str(len(param_encoded)),
               }

    conn.request('POST',uri,headers = headers,body=param_encoded)
    response=conn.getresponse()

    print '\r\n STATUS:  ' + str(response.status) + '   ' + str(response.reason)
    print ' CONTENT: ' + response.read()

    conn.close()