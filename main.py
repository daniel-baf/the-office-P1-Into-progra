# import section
import os

# info section
print("Usuario: Daniel Eduardo Bautista Fuentes")
print("Carnet: 2121323")

# code section
mi_ubicacion = os.getcwd() 

if os.path.exists("modulos"):
    print("La carpeta existe")
else:
    os.mkdir(mi_ubicacion + "/modulos") # cambiando \\ por / por ser linux
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()

