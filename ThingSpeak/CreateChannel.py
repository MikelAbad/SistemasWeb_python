import psutil
import httplib
import urllib

server = 'api.thingspeak.com'
conn = httplib.HTTPConnection(server)
conn.connect()

uri = '/channels'
params = {'api_key': '7ZEVD4MVX39VS4X6',
          'name': 'newChannel',
          'description': 'SW2017 - CPU and RAM',
          'field1': 'CPU',
          'field2': 'RAM',
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