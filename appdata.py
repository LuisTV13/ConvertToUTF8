from os import listdir
from os.path import isfile, join
from src.funtion import Encoding



ruta ='input/'

files = [f for f in listdir(ruta) if isfile(join(ruta, f))]

len = len(files)

encode1 = input("Ingrese el Encoding del archivo original:")
encode2 =input("Ingrese el Encoding del nuevo archivo:")

respuesta = input("Desea Generar archivos(y/n)")

if respuesta == "y":
    print("Archivo generado")
    for n in files:
        for i in range(0,int(len)):
            if n  == files[i]:
                Encoding(ruta+n,encode1,encode2,n)
else:
    print("No se genero ningun archivo")


    