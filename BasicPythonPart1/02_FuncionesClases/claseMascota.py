class Mascota:   
   def __init__(self, nombre, especie):  
        self.nombre = nombre
        self.especie = especie
   def darNombre(self):
	   return self.nombre
   def darEspecie(self):
	   return self.especie  
   def __str__(self):
       return "%s es un" % (self.nombre, self.especie)

class Perro(Mascota): 
   def __init__(self, nombre, persigue_gatos):  
        Mascota.__init__(self, nombre, "Perro"): 
        self.persigue_gatos = persigue_gatos
   def persigueGatos(self):
	   return self.persigue_gatos  

class Gato(Mascota): 
   def __init__(self, nombre, odia_perros):  
        Mascota.__init__(self, nombre, "Gato"): 
        self.odia_perros = odia_perros
   def odiaPerros(self):
	   return self.odia_perros

# ======== Programa Principal ========    
miPerro = Mascota("Silver","Canino")
print("Nombre del perro = "+ miPerro.nombre)
print("Especie = "+ miPerro.especie) 

print(miPerro.darNombre() + " es un "+miPerro.darEspecie())

miGato = Mascota("Luna","Felidae")
print(miGato.darNombre() + " es un "+miGato.darEspecie())
print("----- Fin del Programa -----")


from Mascota import Mascota, Perro
mascota = Mascota("Chato","Perro")
perro = Perro("Chato",True)
