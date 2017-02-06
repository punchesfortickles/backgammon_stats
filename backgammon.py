# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:54:14 2017
 
@author: Nate
"""
 
 
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
def master_list(arg):  
    ary = []
    for i in arg:
        if i!=0.0:    
            ary.append([int(math.floor(i/10.)),
                       int(i-10*int(math.floor(i/10.)))])
    return clean_list(ary)
 
       
def clean_list(arg):
    sum_list = []
    for i in arg:
        if(i[0]<1 or i[1]<1 or i[0]>6 or i[1]>6):
            arg.remove(i)
        else:
            x = int(i[0]+i[1])
            sum_list.append(x)
       
    return sum_list        
   
def histogram(arg):
    No_Rolls = len(arg)
    plt.xlim([2,13])
    x = np.linspace(2,13,No_Rolls)
    plt.plot(x,mlab.normpdf(x,np.average(arg),np.std(arg)))
    plt.hist(arg,bins = [2,3,4,5,6,7,8,9,10,11,12,13],normed =1)
    plt.title("Backgammon")
    plt.grid(True)
    plt.ylabel("# of rolls = {}".format(len(arg)))  
    plt.xlabel('Sum of roll')
    plt.savefig('myfig')
 
if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.readlines()
    contents = [float(x.strip()) for x in content]
    #print(master_list(contents))
    histogram(master_list(contents))
