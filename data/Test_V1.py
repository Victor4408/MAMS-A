import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
nums = range(1,5)




for i in nums:
    f = open('pre_graph'+str(i)+'.txt','r')
    p_G = f.read()
    print(p_G)
    



for i in nums:
    f = open('graph'+str(i)+'.txt','r')
    graph = f.read()
    print(graph)
    





for i in nums :
     f = open('path'+str(i)+'.txt','r')
     path = f.read()
     print(path)
   
path = path+1

for j in range(1,path.size):
    v_size = 1
    

f = np.genfromtxt(fname='pre_graph'+str(4)+'.txt')
print(f)


g= plt.gray(64)
