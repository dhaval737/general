#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 08:29:02 2020

@author: dhavaldangaria
"""

from collections import Counter

def is_permuted(str1,str2):
    if len(str1)!= len(str2):
        return False
    char_set1=[0 for i in range(128)]
    char_set2=[0 for i in range(128)]
    for l in range(len(str1)):
        char_set1[ord(str1[l])] +=1
        char_set2[ord(str2[l])] +=1
        
    print(char_set1)
    if char_set1 == char_set2:
        return True
    
    return False

'''
Using Counter that returns the dictionary of items and their count
'''
def is_permuted_counter(str1,str2):
    if len(str1)!= len(str2):
        return False
    counter=Counter()
    for c in str1:
        counter[c] +=1
    for c in str2:
        if counter[c]==0:
            return False
        counter[c] -=1
    return True
    
s1='dada'
s2='addd'
print(is_permuted(s1,s2))
print(is_permuted_counter(s1,s2))