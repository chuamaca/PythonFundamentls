def SacarFactorial():
    numero=int(input("Ingrese un Numero Positivo: "))
    if numero>0:
        factorial=1;
        for i in range(1, numero+1):
            print(factorial*1)
            factorial=factorial*i
        print(factorial)
    else:
        print("Debes ingresar un Numero Positivo Mayor a 0")

SacarFactorial()