#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:21:57 2020

@author: dhavaldangaria
"""

def heightChecker(heights) -> int:
    
    heights_copy=sorted(heights)
    count=0
    for i in range(len(heights)):
        if heights_copy[i]!=heights[i]:
            count+=1
    return count

def heightChecker1(heights) -> int:
    
    heights_copy=sorted(heights)
    count=0
    for i,j in zip(heights,heights_copy):
        if i!=j:
            count+=1
    return count
    
#print(heightChecker1([1,1,4,2,1,3]))
#print(heightChecker1([5,1,2,3,4]))
#print(heightChecker1([1,2,3,4,5]))

def findMaxConsecutiveOnes(nums) -> int:
    p=0
    q=0
    max_z=0
    cnt=0
    cnt1=0
    for i in range(len(nums)):
        if nums[i]==0:
            p+=1
        if nums[i] == 0 and p > 1:
            p=0
            cnt=0
        else:
            cnt+=1
            if max_z < cnt:
                max_z=cnt
        if p==1 and nums[i] != 0:
            q=1
        if nums[i] == 0 and q > 1 :  
            q=0
            cnt1=0
        if q > 0:
            cnt1+=1
            if nums[i] == 0:
                q+=1
            if max_z < cnt1:
                max_z = cnt1
        print("cnt",cnt)
        print("cnt1",cnt1)
            
        #print(max_z)
    return max_z

def findMaxConsecutiveOnes1(nums) -> int:
    prev,curr,res = 0,0,0
         
    for n in nums:
        if n==1:
            curr+=1
        else:
            res = max(res,curr+prev)
            prev = curr+1   #adding one to prev for flipped 0
            curr = 0
        print('res',res)
        print('curr',curr)
        print('prev',prev)
        print("========================")
    return max(res, prev+curr)


#print(findMaxConsecutiveOnes1([1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1]))
print(findMaxConsecutiveOnes1([1,0,1,1,0]))
#print(findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,1,1,1]))
#print(findMaxConsecutiveOnes([0,0,0,0,0,0,0]))