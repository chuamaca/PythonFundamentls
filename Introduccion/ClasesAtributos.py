class Origen:
    
    def Funcion():
        print("Es una Funcion")

nombre=Origen.Funcion()

print(nombre)

class FabricaTelefonos():
    marca="Lenovo"
    color="Rojo"
    memoriaram=32
    almacenamiento="128 GB"
    
    def llamar(self,mensaje):
        return mensaje
    
    def EscucharMusica(self):
        print("Estas escuchando Musica")


telefono=FabricaTelefonos()
print(telefono)
print(telefono.almacenamiento)


print(telefono.llamar("Hola con quien Hablo"))
telefono.EscucharMusica()
