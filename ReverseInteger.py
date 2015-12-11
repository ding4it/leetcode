#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: ReverseInteger.py
@time: 2015/12/11 17:40
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = True
        if x < 0:
            positive = False
            x = -x
        rs= 0
        radix = 10
        while x:
            tmp = x%radix
            x = x//radix
            rs = rs * 10 + tmp
        if not positive:
            rs = -rs
        print(rs)
        if rs > 1<<31  or rs < -1* 1<<31:
            return 0
        return rs


a = Solution()
a.reverse(-123)