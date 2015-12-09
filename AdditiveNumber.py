#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: AdditiveNumber.py
@time: 2015/11/29 19:30
"""
class Solution(object):
    def check(self,num,i,j,k):
        print(i,j,k)
        a = num[i:j]
        b = num[j:k]
        if len(a)>1 and a[0] == '0':
            return False
        if len(b)>1 and b[0] == '0':
            return False
        c = str(int(a)+int(b))
        if num[k:].startswith(c):
            if len(c)+k == len(num):
                return  True
            return self.check(num,j,k,len(c)+k)
        else:
            return False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1,n//2+1):
            for j in range(i+1,n):
                if self.check(num,0,i,j):
                    return True
        return False

a = Solution()
sss = "0235813"
t = a.isAdditiveNumber(sss)
print(t)