#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  NumberofDigitOne.py
@time: 2016/3/8 22:57
"""
#233
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 :
            return 0
        if n < 10:
            return 1
        radio = 10
        rs = n // 10
        if n % 10 > 0:
            rs += 1
        while n // radio > 0:
            a = n % radio
            b = n // radio//10
            rs += b*radio
            if  (n//radio) % 10 ==1:
                rs += a + 1
            elif (n//radio) % 10 >1:
                rs += radio
            radio = radio * 10
        rs += n //radio
        return rs

a = Solution()
x = a.countDigitOne(20)
print(x)