# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rL3QIgB0vKcV80VG_dcXYKhYXXDBZK7m
"""

list_odd = [1,3,5,7,9] 
list_even = [0,2,4,6,8] 
print(list_odd, list_even) 

list_odd.extend(list_even) 
list_new = list (list_odd) 
print (list_new) 

list_new.sort() 
print(list_new)

list_new = [x*2 for x in(list_new)]
print (list_new) 

for x in list_new:
    print("{} veri tipi: {}".format(x, type(x)))