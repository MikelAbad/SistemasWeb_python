asignaturas=['Sistemas Web',
             'Introduccion a Redes de Computadoras',
             'Diseno de Bases de Datos',
             'Administracion de Base de Datos',
             'Estructuras de Datos y Algoritmos']
print asignaturas

print asignaturas[0] #Posicion 0
print asignaturas[1] #Posicion 1
print asignaturas[-1] #Posicion 1 desde atras
print asignaturas[-2]  #Posicion 2 desde atras
print asignaturas[:2]  #Anteriores a 2
print asignaturas[2:] #Posteriores a 2

for asignatura in asignaturas:
    print asignatura

#Nueva lista con las palabras que contengan 'Dato'
nueva_lista = [i for i in asignaturas if i.find('Dato')!=-1]
print nueva_lista

nueva_lista.append('Gestion de Proyectos')
print nueva_lista

print nueva_lista.index('Gestion de Proyectos')

nueva_lista.remove('Estructuras de Datos y Algoritmos')
print nueva_lista

if 'Gestion de Proyectos' in nueva_lista:
        print 'Esta en la lista'
else:
        print 'No esta en la lista'