#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:27:22 2020

@author: dhavaldangaria
"""


def removeElement(nums, val: int):
    
    i=0
    while i< len(nums):
        if nums[i]==val:
            nums.pop(i)
        else:
            i+=1
    
    return len(nums)
       
#print(removeElement([0,1,2,2,3,0,4,2],2))


def removeDuplicates(nums):
    i=1
    while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
    return len(nums)

def removeDuplicates1(nums):
    j=0
    for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                j+=1
                num[j]=num[i]
    return j+1

print(removeDuplicates([0,0,1,2,2,2,3,4]))