# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:37:18 2021

@author: 5034100
"""
"""
for i in range(array[-1]):
    if i+1 not in array:
        print(i+1)
"""

"""
with O(n)
"""

n = 5
array = [1,2,3,5]
x = int((n*(n+1))/2)
total = 0
for i in array:
    total += i
print(x-total)    
    
