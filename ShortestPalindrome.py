#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  ShortestPalindrome.py
@time: 2016/1/8 20:56
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = s[::-1]
        n = len(s)
        next = [0]*(1+n)
        i,j=0,0

        for i in range(1,n):
            while j > 0 and s[i] != s[j]:
                j = next[j]
            if s[i] == s[j]:
                j += 1
            next[i+1] = j
        j = 0
        for i in range(n):
            while j>0 and rev[i] != s[j]:
                j = next[j]
            if rev[i] == s[j]:
                j += 1
        return rev+s[j:]


a = Solution()
x = a.shortestPalindrome("abcd")
print(x)


    #
    # def shortestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     rev = s[::-1]
    #     n = len(s)
    #     i,j = 0,0
    #     for i in range(1,n):
    #         if s[:(n-i+1)/2] == rev[i:(n-i+1)/2]:
    #             return  rev[:i] + s
    #     return  rev[:-1] + s
