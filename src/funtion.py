import pandas as pd
import numpy as np

output = "output/"

def Encoding(ruta,encoding1,encoding2,n):

    xlx = pd.read_csv(ruta,header=None,sep ='|',encoding=encoding1,dtype =np.object0)
    doc = pd.DataFrame(xlx)
    doc.to_csv(output+n,header=None,sep='|',encoding=encoding2,index=False)

      


    

