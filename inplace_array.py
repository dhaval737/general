#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:33:15 2020

@author: dhavaldangaria
"""

def replaceElements(arr):
    start=0
    big_index=0
    n=len(arr)
    while(True): 
        max_num=0
        for i in range(start, n):
            if arr[i]>max_num:
                max_num=arr[i]
                big_index=i
        for i in range (start, big_index+1):
                arr[i]=arr[big_index]
        print(big_index)
        if (start==big_index and big_index==n-1 ) or big_index==n-1:
            break
        else:
            start=big_index+1
    del arr[0]
    arr.insert(n-1,-1)
    return arr
    
#print(replaceElements([17,18,5,4,6,1]))
#print(replaceElements([57010,40840,69871,14425,70605]))
#print(replaceElements([1,2,3,4,5]))
#print(replaceElements([1,2,5,3,4]))
#print(replaceElements([1,2,8,7,5,6,4,3]))
#print(replaceElements([87366,98734,26121,75644,98748,51614,14537,39842,34419,34376]))

def moveZeroes(nums) -> None:
    p=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[p],nums[i]=nums[i],nums[p]
            p+=1
    print(nums)
            
            
#print(moveZeroes([0,1,0,3,12]))   

def sortArrayByParity( A):
    p=0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[p],A[i]=A[i],A[p]
            p+=1
    return A

def sortArrayByParity1(A):
    i, j = 0, len(A) - 1
    while i < j:
        print("i",i)
        print("j",j)
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]
    
        if A[i] % 2 == 0: i += 1
        if A[j] % 2 == 1: j -= 1
    return A

def sortArrayByParity2(A):
    A.sort(key = lambda x: x % 2)
    return A
    
#print(sortArrayByParity1([3,1,2,4]))   


def sortedSquares(nums) :    
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]    
    #nums.sort()
    return sorted(nums)
print(sortedSquares([-4,-1,0,3,10]))          
            
        