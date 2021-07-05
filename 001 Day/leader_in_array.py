# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:04:16 2021

@author: 5034100
"""
    """
    https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1#
    """
a = [31,40,93,40,98]
a = list(map(int,'63 57 81 36 13 13 21 11 45'.split(' ')))
a = [16,17,4,3,5,2]
# a = [2]
n = len(a)
leaders = []
max_element = a[-1]

leaders.append(max_element)
for i in range(n-2,-1,-1):
    if a[i] >= max_element:
        max_element = a[i]
        leaders.append(max_element)
        
print(leaders[::-1])