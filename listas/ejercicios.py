# ejercicios listas 

# ejercicios manipulación

#1.consiste en la definicion de una lista con elememtos de diferentes tipos y mostrarla en pantalla. como entera como por elementos acceediendo a la posicion de la lista 

print('-----------ejercicio 1---------')
lista= ['Python','Guanenta',2022,'libro',3]
print(lista)
print(lista[0])
print(lista[2])

#2.consite en el uso del operador + para realizar uniones de lista. Ademas,utilizar la funcion len para conocer el numero de elementos que componen la lista 
print('-----------ejercicio 2---------')
lista1=['camiseta','pantalon', 'zapatilla']
lista2=['abrigo','jersey','sudadera','calsetines']

print('numero elemento de la lista1: ', len(lista1))
print('lista1=',lista1)

print('numero elemento de la lista2: ', len(lista2))
print('lista2=',lista2)


lista_contatenada= lista1 + lista2

print('numero elemento de la lista_concatenada: ', len(lista_contatenada))
print('lista_contatenada=',lista_contatenada)


#3.añadir un elemento a la lista de diferentes formas 
print('-----------ejercicio 3---------')
lista=['camiseta','pantalon', 'zapatilla']
lista = lista + ['abrigo']
print(lista)
lista= lista+['sudadera ', 'jersey']
print(lista)
lista= lista + ['bufanda ']

#4. modificar elementos de una lista y borrar elementos de a misma 
print('-----------ejercicio 4---------')
lista=['camiseta','pantalon', 'zapatilla']
print(lista)
lista[1]='casadora'
print(lista )
del lista[0]
print(lista )


#5.uso del operador * que permite contatenar una lista con ella misma un numero finito de veces 
print('-----------ejercicio 5---------')
lista=['camiseta','pantalon', 'zapatilla']
print(lista)
lista_resultante= lista * 3
print(lista_resultante)

#6. creacion de listas como elemento de listas y acceso a dichos elementos
print('-----------ejercicio 6---------')
lista=['camiseta',['calsetines','cazadores'],'zapatillas']

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

#7.extraer una porcion de la lista a una lista nueva 

print('-----------ejercicio 7---------')
lista=[1,2,3,4,5,6,7,8,9]
print(lista)
lista1= lista[3:7]
print(lista1)

lista2=lista[:5]
print(lista2)

lista3= lista[6:]
print(lista3)