# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:26:27 2019

@author: Akanksha
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
data = pd.read_csv('creditcard.csv')
data.head()

g = sns.PairGrid(data=data, vars=['V1','V2','V3','V4','V5','V6','V7','V8','V9','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','28','Amount'], hue='Amount',palette="GnBu_d")
g.map(plt.scatter, s=50, edgecolor="white")
g.add_legend();




