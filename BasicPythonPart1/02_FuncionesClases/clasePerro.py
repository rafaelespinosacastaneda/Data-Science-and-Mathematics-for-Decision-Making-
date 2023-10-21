# Guardado con el nombre de : clasePerro
class Perro:   
    def __init__(self,nombre,raza, peso):
        # variable de instancia única para cada instancia
        self.nombre = nombre 
        self.raza = raza
        self.peso = peso
    def darNombre(self):
	    return self.nombre
    def darRaza(self):
	    return self.raza   
    def darPeso(self):
	    return self.peso   
    def camina(self):
        print(self.nombre+" camina")
    def salta(self):
        print(self.nombre+" salta")	    
    def ladra(self):
        print(self.nombre+" ladra")   
    def olfatea(self):
        print(self.nombre+" olfatea")   
# ======== Programa Principal ========    
miPerro = Perro("Silver","Husky Siberiano",30)

print("Nombre del perro = "+ miPerro.nombre)
print("Raza = "+ miPerro.raza)
print("Peso en kg. = "+str(miPerro.peso))

print("Los métodos se llaman con un punto seguido de un paréntesis. Es importante recordar que no hay que pasar el parámetro self de forma explícita, porque ocurre de forma interna.")


miPerro.camina()
miPerro.salta()
miPerro.ladra()
miPerro.olfatea()

print("----- Fin del Programa -----")