#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  ExcelSheetColumnTitle.py
@time: 2016/1/20 21:35
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        radio = 26;
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rs = ""
        while n>0:
            rem = (n-1)%26;
            n = n//26;
            if rem == 25:
                n = n-1;
            rs +=alpha[rem]
        print(rs[::-1])
        return rs[::-1]

A = Solution()
A.convertToTitle(1)
