#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:28:31 2020

@author: dhavaldangaria
"""


'''
Using set to validate whether
string is unique
'''
def is_Unique_Set(str):
    
    set1=set()
    for ch in str:
        set1.add(ch.lower())
    #print(list(set1))
    
    if len(set1)==len(str):
        print("UNIQUE")
    else:
        print("NOT UNIQUE")


'''
Using dicttionary to validate whether
string is unique
'''        
def is_Unique_Dict(str):
    
    dict1={}
    unique=True
    for ch in str:
        if ch.lower() in dict1:
            unique = False
            break
        else:
            dict1[ch.lower()]=1
    if unique:
        print("UNIQUE")
    else:
        print("NOT UNIQUE")
        
'''
Using ASCII to validate whether
string is unique
'''        
def is_Unique_ascii(str):
    if is_ascii(str):
        if len(str) > 128:
            return False
        char_set=[False for c in range(128)]
        for s in str:
            val=ord(s)
            if char_set[val]:
                return False
            char_set[val]= True
            
    return True

'''
check whether all the characters 
in string are ASCII
'''
def is_ascii(s)  :
    return all(ord(c)<128 for c in s)

#is_Unique_Set("DEV")
#is_Unique_Set("DhavAl")

#is_Unique_Dict("DEV")
#is_Unique_Dict("DhavAl")

print(is_Unique_ascii("DEV"))
`print(is_Unique_ascii("Dhaval"))