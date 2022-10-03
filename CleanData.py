#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:46:35 2022

@author: jorge
"""

import pandas as pd
import matplotlib.pyplot as plt
#print("ruta de DataFrame")
url="gradedata.csv"
df_raw=pd.read_csv(url)
#df_raw=pd.read_csv("gradedata.csv")
df_raw.shape
df_raw.describe()

# define plot_box
def plot_boxplot(df,ft):
    df.boxplot(column=[ft])
    plt.grid(False)
    plt.show()
   
   
   
plot_boxplot(df_raw, "age")  

def outliers(df,ft):
    Q1 = df[ft].quantile(0.25)
    Q3 = df[ft].quantile(0.75)
    IQR= Q3-Q1
    lower_bound = Q1 -1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    ls = df.index[ (df[ft] < lower_bound  )  | (df[ft] > upper_bound) ]
    
    return ls
         
index_list = []
for feature in ["age", "exercise", "hours", "grade"]:
    index_list.extend(outliers(df_raw, feature))

index_list
 
def remove(df, ls):
    ls = sorted(set(ls))
    df = df.drop(ls)
    return df

df_cleaned = remove(df_raw, index_list)
df_cleaned.shape


    