#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:46:35 2022

@author: jorge
"""

### Definicion de Funciones ###
def outliers(df,ft):
    Q1 = df[ft].quantile(0.25)
    Q3 = df[ft].quantile(0.75)
    IQR= Q3-Q1
    Minimum = Q1 -1.5 * IQR
    Maximum = Q3 + 1.5 * IQR
    
    ls = df.index[ (df[ft] < Minimum  )  | (df[ft] > Maximum) ]
    
    return ls

    
def remover_outliers(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df
#####   Fin  #############################


import pandas as pd
url=input("ruta de Base de datos ")

df_raw=pd.read_csv(url)
df_raw.info()
df_raw.describe()



nombres_columnas = list(df_raw.columns)   

print("\n",nombres_columnas)  
index_list = []

for feature in nombres_columnas:
    index_list.extend(outliers(df_raw, feature))

index_list
 


df_cleaned = remover_outliers(df_raw, index_list)
print("\n")
df_cleaned.info()
# Guardamos nos datos sin Outsiders en una archivo csv
df_cleaned.to_csv("DatosLimpios.csv", index=False)

    