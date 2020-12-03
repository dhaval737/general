#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:25:29 2020

@author: dhavaldangaria
"""

def duplicateZeros1(arr) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    i=0
    while i<len(arr):
        print(i)
        if arr[i] == 0:
            for j in range(len(arr)-1,i,-1):
                #print(j)
                arr[j]=arr[j-1]
            print(arr)
            i+=1
        i+=1
    return arr            

#print(duplicateZeros([1,0,2,3,0,4,5,0]))   

lst=[1,0,2,3,0,4,5,0]

#for i in range(len(lst)-1, -1, -1):
#    print(lst[i])
    

def duplicateZeros(arr) -> None:
    dups_poss=0
    length_=len(arr)-1
    
    for left in range(length_+1):
        if left > length_ - dups_poss:
            break
        
        if arr[left]==0:
            if left == length_ - dups_poss:
                arr[length_] = 0 # For this zero we just copy it without duplication.
                length_ -= 1
                break
            dups_poss+=1
    last=length_ - dups_poss
    
    print(last)
    print(dups_poss)
    
    for i in range(last,-1,-1):
        if arr[i]==0:
            arr[i+dups_poss]=0
            dups_poss-=1
            arr[i+dups_poss]=0
            
        else:
            arr[i+dups_poss]=arr[i]
    return arr

#print(duplicateZeros([1,0,2,3,0,4,5,0]))
#print(duplicateZeros([8,4,5,0,0,0,0,7]))


def duplicateZeros2(arr) -> None:
    i=0
    while i<len(arr)-1:
        if arr[i]==0:
            arr.insert(i+1,0)
            arr.pop()
            i+=2
        else:
            i+=1
    return arr

print(duplicateZeros2([8,4,5,0,0,0,0,7]))

                