while True:
    try:
        edad=int(input("Ingrese Su Edad: "))
        print(edad)
        break
    except:
        print("Ingresas una Edad Invalidad")
    finally:
        print("La ejecucion Termino")


while True:
    try:
        num1:int(input("Ingresa un numero: "))
        resultado=100/num1
        print(resultado)
    except ZeroDivisionError:
        print("No se puede Dividir el numero")
