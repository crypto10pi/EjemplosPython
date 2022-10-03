#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:12:27 2021

@author: jorge
"""
lista=["Jorge", "Davila", "Ortiz", 24, 170, 1.79]
print( "Nombre :", lista[0] + " " + lista[1] + " "  )
IMC=lista[4]/lista[5]**2
print("IMC = ", IMC)
if IMC < 18.5:
    print("Peso inferior al normal")
elif  IMC < 24.9:
    print("Peso normal")
elif  IMC  < 30 :
    print("Sobre Peso")
else: 
   print("Obesidad")    
