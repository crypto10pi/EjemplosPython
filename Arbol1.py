#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:57:26 2022

@author: jorge
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data=pd.read_csv("diabetes.csv")
data.info()
data.sample(10)
explicativas=data.drop(["Outcome"], axis=1)
objetivo=data.Outcome
explicativas_train, explicativas_test, objetivo_train, objetivo_test = train_test_split(explicativas,objetivo, test_size=0.2, random_state=0)
modelo= DecisionTreeClassifier(criterion="entropy",max_depth=3)
modelo.fit(explicativas_train, objetivo_train)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(18,12)); plot_tree(decision_tree = modelo, feature_names=explicativas_train.columns, filled=True)