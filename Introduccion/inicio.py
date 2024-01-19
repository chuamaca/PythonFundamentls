print("Hola mundo")

verdadero=True

falso=False

print(verdadero and verdadero)

x=5
print (x> 3 and x < 8)
print ('Resultado :' , x> 3 and x < 8, 'Valor: ', x)

#Operador OR

ticket_invitacion=True
ticket_pagado=False
print('Invitacion: ', ticket_invitacion or ticket_pagado)

#NOR

valor_verdadero= True
resultado_negacion= not valor_verdadero
print('resultado negacion: ', resultado_negacion)

#condicional
edad=20

if edad < 18:
    print("Mayor de Edad")
elif edad>=18 and edad<65:
    print("eres mayor de Edad")
else:
    print("Eres mayor de Edad con experiencia")


# Operador Ternario
mensaje= "Eres mayor de Edad" if edad> 18 else "Eres menor de Edad"



