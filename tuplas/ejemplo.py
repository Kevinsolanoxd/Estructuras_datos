# ------Tuplas---------

tupla=('casa','2',345,'perro',99)
print('Elemetos de la tupla: ',tupla)
print('Elemetos de la posición 0: ',tupla[0])
print('Elemetos de la posición 1: ',tupla[1])
print('Elemetos de la posición 2: ',tupla[2])
print('Elemetos de la posición 3: ',tupla[3])
print('Elemetos de la posición 4: ',tupla[4])

#count: cuenta el número de veces que aparece el elemento indicado como parametro dentro de la tupla.
print('número de elementos 99: ',tupla.count(99))

#index: devuelve la posición de la primera ocurrencia de izquierda a derecha en la tupla del elemento pasado como paralelo

print('Posicioin que ocupa el elemento Perro',tupla.index('perro'))

#n siempre tiene que ser menor que m
#si no se espesifica el valor para n se supone que es 0
#si no se espesifica el valor para m se supone que es el tamaño de la lista menos uno 

tupla= (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

#NumeroElementos=len(tupla)

tupla1=(29,'televisión',8763)
tupla2=(1,2,3,'videojuego')
print('Numero elementos de tupla1: ',len(tupla1))
print('tupla1: ', tupla1)
print('Numero elementos de tupla2: ',len(tupla2))
print('tupla2: ', tupla2)
tupla_concatenada=tupla1+tupla2
print('numero elementos de tuplaconcatenada: ',len(tupla_concatenada))
print('tupla_concatenada: ', tupla_concatenada)

#tupla_resultante=tupla*numero entero 
tupla= (1,2,3,4,5,6,7,8,9)
print(tupla)
tupla_resultante= tupla*4
print(tupla_resultante)


















