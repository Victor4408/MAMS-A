# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import cm
#from colorspacious import cspace_converter
from collections import OrderedDict
#cm.style.use('default')

drawPath = 1
drawPrePath = 0
drawValue = 1
drawEdge = 0
drawText = 0

drawPostSearch = 1
pdfy = 1
agent_number = 4

color_bit = 64
color_bar = np.array([1.0000, 0.9841, 0.9683, 0.9524, 0.9365, 0.9206,
                      0.9048, 0.8889, 0.8730, 0.8571, 0.8413, 0.8254,
                      0.8095, 0.7937, 0.7778, 0.7619, 0.7460, 0.7302,
                      0.7143, 0.6984, 0.6825, 0.6667, 0.6508, 0.6349,
                      0.6190, 0.6032, 0.5873, 0.5714, 0.5556, 0.5397,
                      0.5238, 0.5079, 0.4921, 0.4762, 0.4603, 0.4444,
                      0.4286, 0.4127, 0.3968, 0.3810, 0.3651, 0.3492,
                      0.3333, 0.3175, 0.3016, 0.2857, 0.2698, 0.2540,
                      0.2381, 0.2222, 0.2063, 0.1905, 0.1746, 0.1587,
                      0.1429, 0.1270, 0.1111, 0.0952, 0.0794, 0.0635,
                      0.0476, 0.0317, 0.0159, 0]) 
# =============================================================================
# color_bar = color_bar.reshape(-1,4)
# =============================================================================

# =============================================================================
# color_bar = np.array([1.0000, 0.9841, 0.9683, 0.9524, 0.9365, 0.9206,
#                       0.9048, 0.8889, 0.8730, 0.8571, 0.8413, 0.8254,
#                       0.8095, 0.7937, 0.7778, 0.7619])
# 
# 
# =============================================================================
#PRE-SEARCH 

for agent_i in range(1,agent_number+1):
    preGraph=  np.genfromtxt(fname='pre_graph'+str(agent_i)+'.txt')
# =============================================================================
#     print(preGraph)
# =============================================================================

vertices = preGraph[:,0:3]
values = preGraph[:,3]
edges = preGraph[:,4:]



num_vert = vertices.shape[0]

for j in range(0,num_vert):
    v_size = vertices[j,2]
    if v_size != 0:
        if drawValue:
            val_color = color_bar[math.ceil(values[j]*(color_bit-1))+1]
            ax = plt.gca()
       
# =============================================================================
#             rect = patches.Rectangle((vertices[j,0]-(v_size/2),vertices[j,1]-(v_size/2)),v_size,v_size,angle = 1/v_size,linewidth=1,edgecolor='r',facecolor='gray')
# =============================================================================
            rect1 = plt.Rectangle((vertices[j,0]-(v_size/2),vertices[j,1]-(v_size/2)),width=v_size,height=v_size,angle = (1/v_size),linewidth=1,edgecolor='black',facecolor=str(val_color))
          
            ax.add_patch(rect1)
            plt.axis("scaled")
            
# =============================================================================
#             plt.show()
# =============================================================================
            

       

if drawPostSearch:
    for k in range(1,agent_number+1):
        graph=  np.genfromtxt(fname='graph'+str(k)+'.txt')
        path=  np.genfromtxt(fname='path'+str(k)+'.txt')
        
        vertices = graph[:,0:3]
        values   = graph[:,3]
        edges    = graph[:,4:]
        
        num_ver = vertices.shape[0]
        for i in range(0,num_ver-1):
            v_size = vertices[i,2]
            if v_size !=0:
                
                val_color = color_bar[math.ceil(values[i]*(color_bit-1))+1]
        
                
                ax = plt.gca()
                rect = plt.Rectangle((vertices[i,0]-(v_size/2),vertices[i,1]-(v_size/2)),width=v_size,height=v_size,angle = (1/v_size),linewidth=1,edgecolor='black',facecolor= str(val_color))
                ax.add_patch(rect)
                plt.axis("scaled")
            else:
                    rect = plt.Rectangle((vertices[i,0]-(v_size/2),vertices[i,1]-(v_size/2)),width=v_size,height=v_size,angle = (1/v_size))
                    
if drawPath:
    
    p = path.shape[0]
    for ii in range(0,p):    
        p = path[ii]
        v_size1 = vertices[int(p),2]
    
        if v_size1 !=0:
            
            if ii==1:
                ax = plt.gca()
                rect = plt.Rectangle((vertices[int(p),0]-v_size1/2,vertices[int(p),1]-v_size1/2),width = v_size1,height = v_size1,angle = 1/v_size1, linewidth=3,edgecolor = 'm')
                ax.add_patch(rect)
                plt.axis("scaled")
            else:
                ax = plt.gca()
                rect = plt.Rectangle((vertices[int(p),0]-v_size1/2,vertices[int(p),1]-v_size1/2),width = v_size1,height = v_size1,angle = 1/v_size1, linewidth=3,edgecolor = 'c',facecolor='none')
                ax.add_patch(rect)
                plt.axis("scaled")
                    
