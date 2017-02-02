persona = {'nombre': 'Luz',
           'apellido1': 'Alvarez',
           'apellido2': 'Gutierrez'}
print persona

print persona['nombre']
print persona['apellido1']

for key in persona.keys():
    print key + '=' + persona[key]

persona['ciudad'] = 'Bilbao'

otros_datos = {'fecha-inicio': '2016-01-01',
               'NAN': '12345678-A'}
persona.update(otros_datos)
print persona