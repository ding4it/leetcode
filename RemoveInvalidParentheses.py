#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: RemoveInvalidParentheses.py
@time: 2015/11/29 21:28
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        pars = [0 for i in range(n)]
        sums = [0 for i in range(n)]
        for i in range(n):
            if s[i] == '(':
                pars[i] = 1
            elif s[i] == ')':
                pars[i] = -1
            else:
                pars[i] = 0
        k = 0
        i = 0
        zip = [0]
        while i < n:
            if i< n and pars[i] == 1:
                while i< n and pars[i] == 1:
                    zip[k] += 1
                    i += 1
            elif i< n and pars[i] == -1:
                while i< n and pars[i] == -1:
                    zip[k] -= 1
                    i += 1
            else:
                zip[k] = 0
                i += 1
            k = k + 1
            zip.append(0)
        zip.pop(k)
        print(zip)
        nn = len(zip)
        right = [0 for i in range(nn)]
        right[0]= zip[0]
        allRight = [0 for i in range(nn)]
        allRight[0]= zip[0] if zip[0] < 0 else 0

        for i in range(1,nn):
            right[i] = right[i-1] + zip[i]
            allRight[i]= zip[i] + allRight[i-1] if zip[i] < 0 else allRight[i-1]

        print(right,allRight)

        left = [0 for i in range(nn)]
        left[nn-1] = zip[nn-1]
        for i in range(2,nn+1):
            left[nn-i] = left[nn-i+1] + zip[nn-i]
        print(left)






a = Solution()

sss ="(a)())()"
a.removeInvalidParentheses(sss)
