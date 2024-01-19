def calcular_imc():

    peso=90
    altura=1.64

    imc=peso/(altura ** 2)
    print("IMC: ", imc)

    if imc < 18.5:
        print("Bajo Peso")
    elif imc >=18.5 and imc < 24.9:
        print("Peso Normal")
    else:
        print("Obesidad")

print("Calculando IMD")
calcular_imc()

#Con Imput de Entrada

peso= int(input("Peso: "))
altura=float(input("Altura: "))
result_imc= peso /(altura**2)


print("IMC: ", result_imc )

if result_imc < 18.5:
    print("Bajo Peso")
elif result_imc >=18.5 and result_imc < 24.9:
    print("Peso Normal")
elif result_imc >25 and result_imc < 29.9:
    print("Obesidad")
else:
    print("Sobrepeso")

