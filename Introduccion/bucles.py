mi_lista=[1,2,3,45,6,'Otro']
print(mi_lista)
i=0
for value in mi_lista:
    print(value)
    i+=1
    print('Conteo: ',i)
    
#Range
print("Rangeee")
for i in range(3,5):
    print('Range: ',i)

#While
print("WHileeee")
limit=5
counter=0

while counter<=limit:
    print("Iteracion: " , counter)
    counter+=1
    

print("Retoooooo FOR ")
#Usar Bucle
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
lista_pares, lista_impares=[],[]
pares=0
impar=0
for value in lista:
    if value%2==0:
        pares+=1
        lista_pares.append(value)
    else:
        impar+=1
        lista_impares.append(value)
print('Par:',pares,'Impar: ',impar)
print('Lista Pares: ',lista_pares)
print('Lista Impares: ', lista_impares)


# lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# limite=len(lista2)
# print("Limite: ", limite)
# contador=0
# pares_result=0

# while contador<=limite:
#     contador+=1
#     print('Contador: ', contador)
#     print('Lista Contador ',lista2[contador])


    
    