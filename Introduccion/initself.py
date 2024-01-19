#init  => 
#self  => Uno mismo

class FabricaTelefonos():
    marca="Samsung"
    
    #Tiene los Telefonos Huawei
    def ElaborarHuawei(self):
        self.marca="Huamwei"


telefono=FabricaTelefonos()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)


class FabricaTelefonos02():
    marca='Huawei'
    color='Negro'
    
    def __init__(self):
        print("Estoy ejecuntando el metodo Initi por que se ha creado uno nuevo")


telefono2=FabricaTelefonos02()
