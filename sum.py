# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:00:37 2019

@author: erika
"""

#mod each by 100 then add them all together

def sum(file_name):
    f1 = open(file_name)
    total = 0
    
    for line in f1:   
        total +=int(line)
        
    f1.close()
    return total%10000000000
         
        
print(sum('largenumber.txt'))
