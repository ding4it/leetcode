#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  PalindromePartitioning.py
@time: 2015/12/30 21:39
"""

class Solution(object):
    def isPalindrome(self,s):
        if len(s) <= 1:
            return True
        return list(s) == list(reversed(s))

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if n == 0:
            return [[]]
        elif n == 1:
            return [[s]]
        rs = []
        for i in range(1,n+1):
            pre = s[:i]
            if self.isPalindrome(pre):
                tmpResult = self.partition(s[i:])
                tmpResult = [ [pre] + item for item in tmpResult]
                rs.extend(tmpResult)
        return rs

A = Solution()
x = A.partition("bb")
print(x)