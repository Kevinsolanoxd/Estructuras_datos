# ejercicios listas 

# ejercicios manipulación

#1.consiste en la definicion de una lista con elememtos de diferentes tipos y mostrarla en pantalla. como entera como por elementos acceediendo a la posicion de la lista 


lista= ['Python','Guanenta',2022,'libro',3]
print(lista)
print(lista[0])
print(lista[2])

#2.consite en el uso del operador + para realizar uniones de lista. Ademas,utilizar la funcion len para conocer el numero de elementos que componen la lista 

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
lista=['camiseta','pantalon', 'zapatilla']
lista = lista + ['abrigo']
print(lista)
lista= lista+['sudadera ', 'jersey']
print(lista)
lista= lista + ['bufanda ']

#4. modificar elementos de una lista y borrar elementos de a misma 
lista=['camiseta','pantalon', 'zapatilla']
print(lista)
lista[1]='casadora'
print(lista )
del lista[0]
print(lista )