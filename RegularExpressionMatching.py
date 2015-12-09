#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: RegularExpressionMatching.py
@time: 2015/11/30 9:31
"""
class Solution(object):
    def compare(self,s,p,i,j):
        n = len(s)
        m = len(p)
        print(i,j,n,m)
        if i == n and j == m:
            return True
        if i > n:
            return False
        elif j >= m:
            return False

        if j<m-1 and p[j+1] == '*':
            if j<m-3 and p[j+3] == '*' and ( p[j] == '.' or p[j+2] == '.'):
                pp = p[0:j] + '.' + p[j+3:]
                return self.compare(s,pp,i,j)
            elif j<m-3 and p[j+3] == '*' and p[j] == p[j+2]:
                pp = p[0:j+1] + p[j+3:]
                return self.compare(s,pp,i,j)

            ok = self.compare(s,p,i,j+2)
            if ok:
                return True
            elif i < n and  p[j] == '.':
                ok = self.compare(s,p,i+1,j)
                if ok:
                    return True
            elif i < n and s[i] == p[j]:
                ok = self.compare(s,p,i+1,j)
                if ok:
                    return True
        elif  j<m and i< n and (p[j] == '.' or p[j] == s[i]):
            ok = self.compare(s,p,i+1,j+1)
            if ok:
                return True
        return False




    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.compare(s,p,0,0)

a = Solution()

s = "bbabacccbcbbcaaab"
p = "a*b*a*a*c*aa*c*bc*"
tt = a.isMatch(s,p)
print(tt)