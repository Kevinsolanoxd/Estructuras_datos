# Ejercicios


diassemanaingles= {'Lunes': 'Monday', 'Martes': 'Tuesday','Miercoles': 'Wednesday','Jueves':'Thursday','Viernes': 'Friday'}


print(diassemanaingles['Lunes'])
print(diassemanaingles['Miercoles'])
print(diassemanaingles['Viernes'])


diassemanaingles= {'Lunes': 'Monday', 'Martes': 'Tuesday','Miercoles': 'Wednesday','Jueves':'Thursday','Viernes': 'Friday'}
print(diassemanaingles)
diassemanaingles['Sabado']= 'Saturday'
print(diassemanaingles)
diassemanaingles['Domingo']= 'Sunday'
print(diassemanaingles)
diassemanaingles['Lunes']= 'MondayBORRAR'
print(diassemanaingles)

diassemanaingles= {'Lunes': 'Monday', 'Martes': 'Tuesday','Miercoles': 'Wednesday','Jueves':'Thursday','Viernes': 'Friday'}

print('Número de elementos de diccionario: ', len(diassemanaingles))
print('Elemento mayor del diccionario: ',max(diassemanaingles))
print('Elemento menor del diccionario: ',min(diassemanaingles))


diassemanaingles= {'Lunes': 'Monday', 'Martes': 'Tuesday','Miercoles': 'Wednesday','Jueves':'Thursday','Viernes': 'Friday'}
print('Diccionario original: ',diassemanaingles)
diccionariocopia=diassemanaingles.copy()
print('Diccionario copy: ',diccionariocopia)
print('Valor del lunes (pop): ',diassemanaingles.pop('Lunes'))
print('Diccionario despues del pop: ',diassemanaingles)
print('Elemento al azar con popitem: ',diassemanaingles.popitem())
print('Diccionario despues del popitem: ',diassemanaingles)
print('Valor del Martes (get): ',diassemanaingles.get('Martes'))
print('Valor del lunes (get) (no existe): ',diassemanaingles.get('Lunes'))
print('Valor del lunes (get) (no existe): ',diassemanaingles.get('Lunes','No existe'))
diassemanaingles.update({'Lunes':'MondayNUEVO','Martes':'Tuesday'})
print('Diccionario después del update: ',diassemanaingles)
print('setdeafult del Sábado: ',diassemanaingles.setdefault('Sabado','Saturday'))
print('Diccionario después del setdefault (nuevo elemento): ',diassemanaingles)
print('setdefault del Lunes: ',diassemanaingles.setdefault('Lunes','Lunes'))
print('Diccionario despues del setdefault (elemento existente): ',diassemanaingles)
print('Elemento iterable (items): ',diassemanaingles.items())
print('Elemento iterable (claves): ',diassemanaingles.keys())
print('Elemento iterable (valores): ',diassemanaingles.values())
print('Diccionario después del clear: ',diassemanaingles.clear())








































