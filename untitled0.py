# -*- coding: utf-8 -*-
"""
Created on April '20'

@author: Sohom Chatterjee
"""
#%% IMPORTING LIBRARIES
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import mmread
import os, glob, re
import sys
import string
#%% FILE READ (FACEBOOK NETWORK)
##Read .mtx file as nxGraph
if __name__ == "__main__":
    # load mtx files
    path ='C:/Users/Sohom/Desktop/ISEN 689/' 
    # os.path.dirname(os.path.realpath(__file__)) + '/'''
    data_path = path + 'Data/'
    # data_path = '/Users/rw422/Documents/Twitter/AV Events Keywords Only (csv)''
    
    filename = 'socfb-American75'
    # glob.glob(data_path + '*.csv')[:1]''
    
    df = mmread(data_path + filename+'.mtx')
     


G = nx.from_scipy_sparse_matrix(df)
#%% GEPHI VISUALIZATION
if __name__ == "__main__":
    
    gephi_path = path + 'Gephi/'

    nx.write_gexf(G, gephi_path + filename + '.gexf')
#%% 