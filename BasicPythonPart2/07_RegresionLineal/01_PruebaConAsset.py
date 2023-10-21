# Guardado con el nombre de 01_PruebaConAsset.py
import unittest
  
# Probando con clases (class) 
class Myclass:
    x = 5
   
class Myclass2:
    x = 6
   
class PruebaClass(unittest.TestCase):
    # función de prueba para probar si obj es una instancia de clase
    def prueba_negativa(self):
        objectName = Myclass()
        # mensaje de error en caso de que falle el caso de prueba
        mensaje = "El objeto dado no es una instancia de Myclass."
       
        # assertIsInstance() para verificar si obj es una instancia de clase
        self.assertIsInstance(objectName, Myclass2, mensaje)
  
# ----- Programa Principal ----- 
print("----- Programa Principal -----")
if __name__ == '__main__':
    unittest.main()