from os import listdir
from os.path import isfile, join
from src.funtion import Encoding



ruta ='input/'

files = [f for f in listdir(ruta) if isfile(join(ruta, f))]

len = len(files)

encode1 ='UTF-8'
encode2 ='UTF-16'


for n in files:
    for i in range(0,int(len)):
        if n  == files[i]:
            Encoding(ruta+n,encode1,encode2,n)

    

    


