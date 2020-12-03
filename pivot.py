#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:15:53 2020
@author: dhavaldangaria
"""

def pivotIndex(nums) -> int:
    
    n=len(nums)
    p=n//2
    right=0
    left=0
    while(p>0 and p<n-1):
        left=sum(nums[:p])
        right=sum(nums[p+1:])
        if left==right:
            return p
        elif abs(left)>abs(right):
            p-=1
        else:
            p+=1
    return -1

def pivotIndex1(nums) -> int:
    
    total=sum(nums)
    add=0
    for i in range(len(nums)):
        if add == total - nums[i] - add:
            return i
        #if add > total - nums[i] - add:
        #    break
        add+=nums[i]
    return -1
print(pivotIndex1([1,7,3,6,5,6]))
print(pivotIndex1([1,2,3]))
print(pivotIndex1([-1,-1,-1,-1,-1,0]))
print(pivotIndex1([-1,-1,-1,-1,-1,-1]))
    