#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:04:03 2021

@author: jorge
"""

edad= int(input("¿Que edad tienes? "))
if edad < 0:
    print("No hay edades negativas")
if  0 <= edad <18:
    print("Eres un menor de edad")
if 18 <= edad < 30 :
    print("Eres un adulto")
if 30 <= edad < 60 :
    print("eres un adulto mayor")
else:
    print("Eres un adulto en Plenitud")    
      
