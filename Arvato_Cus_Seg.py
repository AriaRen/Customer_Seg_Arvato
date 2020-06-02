# import libraries here; add more as necessary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# magic word for producing visualizations in notebook
%matplotlib inline


#Load Data
azdias = pd.read_csv('../../data/Term2/capstone/arvato_data/Udacity_AZDIAS_052018.csv', sep=';')
customers = pd.read_csv('../../data/Term2/capstone/arvato_data/Udacity_CUSTOMERS_052018.csv', sep=';')

#Clean data and remove NA.
azdias = azdias.dropna(axis=1, thresh=.7*azdias.shape[0])
azdias = azdias.dropna(axis=0, thresh=.7*azdias.shape[1])
azdias = azdias.dropna()














