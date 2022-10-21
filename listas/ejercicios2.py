#ejercicios listas 

# Metodos propios

from operator import index


lista=[45,32,3,78]
print('Lista original: ',lista)
# función append: añade un elelmnto a la lista 
lista.append(995)
lista.append(7)
print('lista despues de usar append: ',lista )
#función sort organiza la listra 
lista.sort()
print('lista ordenada: ',lista )
#función reverse revierte el orden de la lista 

lista.reverse()
print('lista alreves: ',lista)
#función extend: añade un elemento de una lista a otra lista 
lista_extend=[1,5,87,45]
lista.extend(lista_extend)
print('lista despues de exted: ',lista)
#función count: cuenta el numero de veces que se repite un elemento indicado 
print('numero de elementos 45: ' ,lista.count(45))
#Función insert: añade elemento pasado como parametro a la lista en la pocicion indicada tambien con parametro
lista.insert(4,111)
print('lista despues de insert: ',lista )

#Función remove: elimina la primera ocurriencia empezando por la izquierda de la lista indicado como paralelo

lista.remove(45)
print('lista despues de remove: ',lista)

#Función index:devuelve la pocicion de la primera ocurrencia de izquierda a derecha de la lista,del elemento pasado como paralelo
print('pocicion del elemnto 111: ',lista,index(111))

#Función pop:
lista.pop()
print('lista despues de pop: ',lista)
#Función clear: elimina todos los elementos de la lsita 
lista.clear()
print('lista despues de clear: ',lista)
