#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:33:52 2021

@author: jorge
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({'x':[1,3,5,7,9,11],'y':[10,25,35,33,41,59]})
df
sns.lmplot(x='x', y='y', data=df)