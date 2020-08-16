# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


days = [1,2,3,4,5,6]
temperature = [34.5,43.5,39.6,44.5,34.5,35.6]

sns.lineplot(days,temperature)
graph_df = pd.DataFrame({'days':days,'temperature':temperature})
sns.lineplot(x='days',y='temperature', data=graph_df)


df = sns.load_dataset('tips')
df.head()

sns.lineplot(x='total_bill', y='tip', data=df)