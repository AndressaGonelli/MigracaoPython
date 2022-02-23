import pandas as pd
import os
from datetime import datetime

path = os.path.abspath(".")

for i in range(1,5):
    caminho=f"{path}\\arquivos_carga_csv\\clients-{i:03d}.csv"
    if i == 1:
      temp = pd.read_csv(caminho, header=0, keep_default_na=False, sep=";")
      df2 = temp

    else:
      col_name = df2.columns
      temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
      df2 =  pd.concat([temp,df2])

df2.reset_index()
#df.reset_index()

#df.to_csv('resultado.csv', index=False)
print(df2.to_csv(index=False))

'''
for i in range(1,10):
  caminho=f"{path}\\arquivos_carga_csv\\transaction-in-{i:03d}.csv"
  
  if i == 1:
    temp = pd.read_csv(caminho, header=0, keep_default_na=False, sep=";")
    df = temp

  else:
    col_name = df.columns
    temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
    df =  pd.concat([temp,df])

    

for i in range(1,64):
  caminho=f"{path}\\arquivos_carga_csv\\transaction-out-{i:03d}.csv"
  col_name = df.columns
  if i == 1:
    temp = pd.read_csv(caminho, header=None,skiprows=1, keep_default_na=False, sep=";",names=col_name)

  else:
    col_name = df.columns
    temp = pd.read_csv(caminho, header=None, keep_default_na=False, sep=";", names=col_name)
  df =  pd.concat([temp,df])
'''
  
