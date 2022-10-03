#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:17:47 2022

@author: jorge
"""
l=[]
peso=float(input("Dame tu peso en Kgr = "))
l.append(peso)
altura=float(input("Tu altura en metros = "))
l.append(altura)
IMC=round(peso/altura, 3)

print("IMC =", IMC)
print(l)