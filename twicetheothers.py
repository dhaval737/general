#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:55:59 2020

@author: dhavaldangaria
"""

def dominantIndex(nums) -> int:
    first=-float('inf')
    second=-float('inf')
    index=0 
    for i in range(len(nums)):
        if nums[i]>first:
            second,first=first,nums[i]
            index = i
        if nums[i]<first and nums[i] > second:
            second=nums[i]        
    if first >= 2 * second:
        return index
    else:
        return -1    
    
def dominantIndex1(nums) -> int:    
    if len(nums)<2:
        return 0
    first,second=0,0 
    for i in range(1,len(nums)):
        if nums[i]>nums[first]:
            second,first=first,i
        else:
            if first==second:
                second=i
            else:
                if nums[i] > nums[second]:
                    second=nums[i]    
        
    if nums[first] >= 2 * nums[second]:
        return first
    else:
        return -1 
print(dominantIndex([3, 6, 1, 0]))    
print(dominantIndex([1, 2, 3, 4]))            
        