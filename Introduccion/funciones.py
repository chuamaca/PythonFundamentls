#Funcion
#def sumar(a,b):
#    print("Hola mundo Python")
#    rta=a+b
#    print('Suma:' ,rta)
#
#def sumar3(j,l,m):
#    print("Hola mundo Python 2")
#    rta=j+l+m
#    print('Suma:' ,rta)

#sumar(2,4)
#sumar3(5,5,5)


lista=[]

num=0

def pedir():
    i=0;
    while i<=5:
        num=float(input("Ingresa un Numero: "))
        lista.append(num)
        i+=1


def ordernarPares():
    lista.sort()
    pares=[]
    impares=[]
    for item in lista:
        if item%2==0:
            pares.append(item)
        else:
            impares.append(item)
        
        print(pares)
        print(impares)


pedir()
ordernarPares()


