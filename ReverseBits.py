#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  ReverseBits.py
@time: 2016/1/6 10:24
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rs = 0
        i = 0
        x = 1
        while n:
            rs =rs * 2 + n % 2
            n = n //2
            i +=1
        rs <<= 32-i
        return rs

A =  Solution()
x = A.reverseBits(1 )
print(x)