#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:57:35 2020

@author: dhavaldangaria
"""

def thirdMax(nums) -> int:
    if len(nums) == 0:
        return 0
    else:
        nums=list(set(nums))
        if len(nums) < 3:
            return max(nums)
        return sorted(nums)[-3]

def thirdMax1(nums) -> int:
    maximums = set()
    for num in nums:
        maximums.add(num)
        if len(maximums) > 3:
            maximums.remove(min(maximums))
    if len(maximums) == 3:
        return min(maximums)
    return max(maximums)
        
print(thirdMax1([2,2,3,1]))