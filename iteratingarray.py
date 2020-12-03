#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:17:04 2020

@author: dhavaldangaria
"""

def checkIfExist( arr) -> bool:
    
    if arr.count(0) > 0 and arr.count(0)%2==0:
        return True
    for i in arr:    
        print(i)
        print(2*i)
        if 2 * i in arr and  i!=0:
            return True
    
        
    return False

#print(checkIfExist([-2,0,10,-19,4,6,-8]))
 
lst=[0,0,5]  
#print(lst.count(0)) 

def validMountainArray(arr):
    if len(arr) < 3:
        return False
    peak=-1
    is_peaked= False
    
    bottom=-1
    for i in range(len(arr)-1):
        if arr[i+1]==arr[i]:
            return False
        if peak<0:
            if arr[i+1]<arr[i]:
                return False  
        peak=i
        if arr[i+1]<arr[i] and peak > 0 :
            is_peaked= True
            
        
        if is_peaked:
            if arr[i+1]>arr[i]:
                return False
            bottom=i
    return True and bottom >= 0
            
def validMountainArray1(arr):
    l = len(arr)
    i=0
    while i<l-1 and arr[i]<arr[i+1]:
        i+=1
    
    if i==0 or i==l-1:
        return False
    
    while i<l-1 and arr[i]>arr[i+1]:
        i+=1
        
    return i==l-1
    
    
print(validMountainArray1([2,1]))
print(validMountainArray1([3,5,5]))
print(validMountainArray1([0,3,2,1]))
print(validMountainArray1([0,1,2,3,4,5,6,7,8,9]))
    