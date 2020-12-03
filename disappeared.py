#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:38:51 2020

@author: dhavaldangaria
"""

def findDisappearedNumbers(nums) :
    missing=[]
    l=len(nums)
    p=0
    if l==0:
        return missing
    nums=sorted(list(set(nums)))
    l1=len(nums)
    for i in range(1,l+1):
        if p<l1 and i == nums[p]:
            p+=1
        else:
            missing.append(i)
    return missing

def findDisappearedNumbers1(nums) :
    nums_set = set(nums)
    n = len(nums)+1
    missing_number = []
    for number in range(1, n):
        if number not in nums_set:
            missing_number.append(number)
    return missing_number


#print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers1([1,1]))