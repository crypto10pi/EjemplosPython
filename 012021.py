#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:17:03 2022

@author: jorge
"""
edad = int(input("Que edad tienes\t"))
if edad <= 0:
    print("No hay edades Negativas")
if 0 <edad < 18:
    print("Eres un menor de edad")
if 18 <= edad < 30:
    print("Eres en adulto")
    
   
    