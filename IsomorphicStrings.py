#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: IsomorphicStrings.py
@time: 2015/12/11 17:09
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = dict()
        n = len(s)
        sss = set()
        for i,ch in enumerate(s):
            if d.get(ch) and d.get(ch) != t[i]:
                return False
            elif d.get(ch) and d.get(ch) == t[i]:
                continue
            elif d.get(ch) == None and t[i] in sss:
                return False
            else:
                d[ch] = t[i]
                sss.add(t[i])
        return True

a = Solution()
s ="aa"
t = "bb"
xx = a.isIsomorphic(s,t)
print(xx)