# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:18:07 2019

@author: aambrioso
"""

from decimal import *

bal = Decimal('1500')
r = Decimal('.1825')
pay = Decimal('117.83')
tot_int = Decimal('0')


while bal > 0:
    print(round(bal,2), round(tot_int,2))
    int= bal*r/12
    if bal < 117.83:
        last_bal = bal
        last_total_int = tot_int
    bal = bal - pay + int
    tot_int+=int
    
int = last_bal*r/12
tot_int = last_total_int+int
bal -=bal
print(round(bal,2), round(tot_int,2))  
    
