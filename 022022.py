#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:12:46 2022

@author: jorge
"""

edad=int(input("¿ Que edad tienes?"))
if edad <= 0:
    print("No hay edad Negativa")
elif  edad < 18:
    print("eres menor de edad")
elif edad < 30:
    print("Eres un adulto") 
else: print("Eres un adulto en Plenitud")    