# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:59:18 2020

@author: vilktor
"""

import matplotlib.pyplot as plt
import numpy as np
def checker(s):
    temp=[]
    
    for i in s:
        if i.isdigit():
            
            temp.append(i)
    
    avg=temp[0]+'.'+temp[1]+temp[2]+temp[3]
    #median=temp[4]+'.'+temp[5]
    return avg
        
    
fil_name="course.txt"
title=''
prof_name=[]
average=[]

with open(fil_name,'r') as t:
    for x in t:
        i=x.split()
        if len(i)==4:
            
            title=x
        
        if len(i)>4:
            prof_name.append(i[0]+' '+i[2][:-1])
            average.append(float(checker(x))*25)
        

fig=plt.figure()
ax=fig.add_axes([2,2,2,2])#addjust the size of graph

plt.bar(prof_name,average,width=0.5,color=["green"])
plt.title(title) 
plt.ylabel('GPA in percent(%)') 
plt.xlabel("Professor's name") 
         
            
                
            

                
                 
            
                                   
                
            
    