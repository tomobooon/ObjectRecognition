# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:07:32 2021

@author: Tomohiro
"""


"""
w = open('new_tfdict.txt', 'w')
f = open('tensorflow_dict.txt', 'r')
for i, line in enumerate(f):
    if i % 4 == 0:
        continue
    elif i % 4 == 3:
        continue
    else:
        w.writelines(line)
    
w.close()
f.close()
"""


f = open('new_tfdict.txt', 'r')
w = open('new_tfdict2.txt', 'w')

for i, line in enumerate(f):
        
    t1 = line.replace(' ', '')
    t1 = t1.replace('id:', ',')
    t1 = t1.replace('\n', '')
    t1 = t1.replace('display_name', '')
    w.writelines(t1)
    
w.close()
f.close()