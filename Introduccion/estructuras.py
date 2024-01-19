##Listas
#Colleccion
mi_lista=[1,2,3,4,'Hola Mundo']
print(mi_lista)
#Agrega
mi_lista.append("otros")
print(mi_lista)
#remover por valor
mi_lista.remove("Hola Mundo")
print(mi_lista)

#remover por posicion
mi_lista.pop(0)
print(mi_lista)

#modificar por posicion
mi_lista[1]="Otros 2"
print(mi_lista)


#Buscar ELemento - Retorna V, F
print(2 in mi_lista)
print(100 not in mi_lista)

#Acceder al ultimo elemento de la Lista
print(mi_lista[-1])

#Acceder al ultimo elemento de la Lista
print(mi_lista[-1])

#Numero de elementos de nuestra Lista
print(len(mi_lista))
print(type(mi_lista))

########### TUPLAS #########
#Son Inmutables, es decir no se puede modificar una vez declarada
mi_tupla=(1,2,(3,2),4,5,"Sies")
print(mi_tupla)
#Sus indices siempre empiezan en 0
print(mi_tupla[1])

print(len(mi_tupla))
print(3 in mi_tupla)
print(type(mi_tupla))
#
#Al igual que las listas, las tuplas también pueden ser anidadas.


print(mi_tupla[2][0])


############  Conjuntos
conjunto_vacio=set()

############   Diccionarios
print("Dicccionarios")
mi_diccionario={}
mi_diccionario={'1':'uno','2':'Dos','3':'Tres'}
print(mi_diccionario)
print(type(mi_diccionario))

otro_diccionario={}
otro_diccionario=dict(clave1='Clase 01', clave2='Clase 02')
print(otro_diccionario)
#Acceder al valor de una clave
valor_extraido=otro_diccionario['clave2']
print(valor_extraido)
#Modificar el valor asociado a una clave
otro_diccionario['clave2']='Clase 02 Modificado'
print(otro_diccionario)

#Crear DIcionario con otro
dicc={'01':otro_diccionario,'02':mi_diccionario}
print(dicc)

#Consultar
print('01' in dicc)

#Eliminar
del otro_diccionario['clave1']
print("Elimianr",otro_diccionario)

##Lista De Diccionarios

dict_list=[]
dic001={'01':'Peru','02':'Argentina','03':'Brazil'}
dict_list.append(dic001)
print(dict_list)
dic001={'01':'Mexico','02':'Argentina','03':'Brazil','04':'Uruguay'}
dict_list.append(dic001)
print(str(dict_list))

#En Varias Lineas Acceder al elemento del Diccionario
elemento_lista=dict_list[1]
print(elemento_lista)
print(elemento_lista['03'])
#En una Sola Linea
una_linea=dict_list[1]['01']
print(una_linea)



