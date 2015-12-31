#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  PalindromePartitioning2.py
@time: 2015/12/30 22:09
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pal = [[False]*(n+1) for i in range(n+1)]
        cut = [0]*n
        for i in range(n):
            pal[i][i] = True
        for i in range(1,n):
            minn = cut[i-1] + 1
            for j in range(i):
                if s[j] == s[i] and (j+1 == i or pal[j+1][i-1]):
                    pal[j][i] = True
                    print(j,i)
                    tmpmin = cut[j-1] + 1 if j > 0 else 0
                    minn = tmpmin if minn > tmpmin else minn
            cut[i] = minn

        return cut[n-1]



A = Solution()
x = A.minCut("cdd")
print(x)