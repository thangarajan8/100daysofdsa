# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:54:29 2021

@author: Thangarajan
Solved using sliding windows

"""

arr = list(map(int,'135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134'.split(' ')))
s = 468
n = len(arr)

    
total = 0
inc = 0
for i in range(n):
    total = total+arr[i]
    while total > s:
        total -= arr[inc]
        inc = inc+ 1
    if total == s:
        print(inc+1,i+1,total)
        break
    
        
    