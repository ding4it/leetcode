#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  DecodeWays.py
@time: 2016/1/1 19:50
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        vec = [-1]*n
        def step(s,start):
            if start >= n:
                return 1
            if s[start] == '0':
                vec[start] = 0
                return 0
            if start == n -1:
                vec[start] = 1
                return 1
            if vec[start] > -1:
                return vec[start]
            if s[start] > '2':
                vec[start] = step(s,start+1)
                return vec[start]
            elif s[start] == '1' or (start < n-1 and s[start+1] < '7'):
                vec[start] = step(s,start+2) + step(s,start+1)
                return vec[start]
            else:
                vec[start] =step(s,start+1)
                return vec[start]
        if s == "":
            return 0
        tmp = step(s,0)
        print(vec)
        return tmp


A = Solution()
A.numDecodings("46733513432327145287876221448289496868141159786577636892519189412286455756583388154956478171946599201")