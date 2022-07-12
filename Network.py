# -*- coding: utf-8 -*-
"""
Created on April '20'

@author: Sohom Chatterjee
"""
#%% 1. IMPORTING LIBRARIES
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import mmread
import os, glob, re
import sys
import string
import math
from tqdm import tqdm
from scipy import optimize
#%% 2. FILE READ (FACEBOOK NETWORK)
##Read .mtx file as nxGraph
if __name__ == "__main__":
    # load mtx files
    path ='C:/Users/Sohom/Desktop/ISEN 689/' 
    # os.path.dirname(os.path.realpath(__file__)) + '/'''
    data_path = path + 'Data/'
    # data_path = '/Users/rw422/Documents/Twitter/AV Events Keywords Only (csv)''
    
    filename = 'socfb-Reed98'
    # glob.glob(data_path + '*.csv')[:1]''
    
    df = mmread(data_path + filename+'.mtx')
     
Gr = nx.from_scipy_sparse_matrix(df)
#%% 3. GEPHI VISUALIZATION
if __name__ == "__main__":
    
    gephi_path = path + 'Gephi/'

    nx.write_gexf(Gr, gephi_path + filename + '.gexf')
#%% 4. FUNCTIONS

def avg_degree(G):
     a=0
     for node in G.nodes(): 
         a = a+ G.degree[node]
     return(a/len(G.nodes()))

def total_degree(G):
    td=0
    for node in  G.nodes():
        td = td + G.degree(node)
    return td
        
def randflip():
    return np.random.uniform(low=0.0, high=1.0, size=None)

def expand_scale_free(G):
    if randflip()<=birth_rate:
        G.add_node(len(G.nodes())) #ONLY CREATING NODE 
        for node in range(0,len(G.nodes)-1): #CREATING EDGES
            if randflip()<=G.degree(node)/total_degree(G):
                G.add_edge(node,len(G.nodes())-1) 
            
def assign_initial_node(G):
    for node in G.nodes(): 
        if G.degree[node] ==math.ceil(avg_degree(G)): 
            status[node]=1
            break
#%% 5. CONSTANTS

birth_rate=0.4
inf_rate=0.35
rec_rate=0.38
#%% 6. LISTS AND STARTING CONDITIONS
G=Gr.copy() #We keep a copy of the graph to keep the original undistorted

#Status List (1:Infected, 0:Healthy)
status= np.zeros((len(G.nodes()),), dtype=int)
#Select initial infected node
assign_initial_node(G)
# #infect intial node
# status[assign_initial_node(G)]=1

#status[3]=1
#Lists
infC=[1] #Count of Total Infected People, per time stage
infR=[] #Ratio of Total Infected People, per time stage
susC=[len(G.nodes())-1] #Count of Total Healthy People, per time stage
susR=[] #Ratio of Total Healthy People, per time stage
#%%  7. BASIC ALGORITHM
count=0
while sum(status)>0 or count==200:
    ##Update system as per logic
    InfectedList=[]

    #Update ill nodes
    for edge in G.edges():
        u=edge[0]
        v=edge[1]
        if status[u]==1 and status[v]==0 and randflip() <= inf_rate:
            InfectedList.append(v)
    for ele in range(0,len(InfectedList)):    
        status[InfectedList[ele]]=1
        
    #Update healthy nodes
    for ele in range(0,len(status)): 
        if status[ele]==1 and randflip()<=rec_rate: 
           status[ele]=0
           
    #Count and add to array
    i=sum(status)
    infC.append(i)
    susC.append(len(G.nodes()) - i)
    infR.append(sum(status)/len(G.nodes()))
    # #Code to expand network (scale-free)
    expand_scale_free(G)
    # #status append for new node
    status=np.append(status,0)
    count=count+1
    print('Iteration:'+ str(count))
    print('Infected Count:' + str(sum(status)))
    print('Infected Ratio:' + str(sum(status)/len(G.nodes())))
    print('-----------------------------------------------------')
   
#%% SAVE VALUES IN ARRAY

a=[]
for ele in range(0,len(infC)):
    a.append(infC[ele]/len(G))
infRatio=a    
x= list(range(0,len(infRatio)))
y=infRatio
fig, tst = plt.subplots()
tst.plot(x35, y35, '.', label='\u03B2=0.35')
tst.plot(x, y, '.', label='\u03B2(lds)=0.35')
tst.set_xlim([0, 175])
tst.set_ylim([0, 1])
legend = tst.legend(loc='upper right', shadow=True, fontsize='medium')
plt.show()
#%% PLOT CURVE

infRatio = np.array(infR)

fig, I_t = plt.subplots()
I_t.plot(x35, y35, '.', label='\u03B2=0.35')
I_t.plot(x25, y25, '.', label='\u03B2=0.25')
I_t.plot(x15, y15, '.', label='\u03B2=1.5')
I_t.set_xlim([0, 175])
I_t.set_ylim([0, 1])
I_t.set_xlabel("t",style='italic')
I_t.set_ylabel("I(t)", style='italic')
legend = I_t.legend(loc='upper right', shadow=True, fontsize='medium')


plt.show()
#%% 4. EXPANSION TESTING
if __name__ == "__main__":
    
    gephi_path = path + 'Gephi/'

    nx.write_gexf(Gr, gephi_path + filename + 'testafterforloopindent.gexf')


