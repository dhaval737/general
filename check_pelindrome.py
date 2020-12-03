#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:00:35 2020

@author: dhavaldangaria
"""
from collections import Counter
import unittest

def is_pelindrome_permutation(str):
    counter=Counter()
    str=str.lower()
    for s in str:
        if s != " ":
            if counter[s] > 0:
                counter[s]-=1
            else:
                counter[s]+=1
    
    #print(counter)
    print(sum(counter.values()))
    if sum(counter.values()) ==1 or  sum(counter.values()) ==0:
        return True
    return False
    
#print(is_pelindrome_permutation("abcab"))

'''print(is_pelindrome_permutation("Tact Coa"))
print(is_pelindrome_permutation("jhsabckuj ahjsbckj"))
print(is_pelindrome_permutation("Able was I ere I saw Elba"))
print(is_pelindrome_permutation("So patient a nurse to nurse a patient so"))
print(is_pelindrome_permutation("Random Words"))
print(is_pelindrome_permutation("Not a Palindrome"))
print(is_pelindrome_permutation("no x in nixon"))
print(is_pelindrome_permutation("azAZ"))
'''

class Test(unittest.TestCase):
 
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = is_pelindrome_permutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()