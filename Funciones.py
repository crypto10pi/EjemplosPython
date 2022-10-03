#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:29:02 2022

@author: jorge
"""

l=[]
def  Cuadrado(x):
    return x**2
#Definimos la funcion Datos    
def Datos(l):
    nombre=input("Nombre:")
    ApellidoPaterno=input("Apelliodo Paterno: ")
    ApellidoMaterno=input("Apellido Materno: ")
    Peso=float(input("Peso: "))
    Edad=int(input("Edad: "))
    l.append(nombre)
    l.append(ApellidoPaterno)
    l.append(ApellidoMaterno)
    l.append(Peso)
    l.append(Edad)
x=float(input("dame el numero x = " ))
y= Cuadrado(x)
print(y)
Datos(l)
print(l)


    