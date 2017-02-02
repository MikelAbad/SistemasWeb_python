persona = {
    'id': 'mlalvgut',
    'desc': {
        'firstName': 'Luz',
        'lastNames': ['Alvarez', 'Gurierrez']
    },
    'contact': {
        'email': 'marialuz.alvarez@ehu.es',
        'phone': '94614462'
    },
    'courses': [
        {'code': 27699,
         'desc': 'Introduction to Computer Netwroks'
        },
        {'code': 27702,
         'desc': 'Web Systems'
        }
    ]
}

print persona

id = persona['id']
print id

firstName = persona['desc']['firstName']
print firstName

lastName1 = persona['desc']['lastNames'][0]
lastName2 = persona['desc']['lastNames'][1]
print lastName1 + ' ' + lastName2

email = persona['contact']['email']
print email

phone = persona['contact']['phone']
print phone