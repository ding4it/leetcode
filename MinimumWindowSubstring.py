#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  MinimumWindowSubstring.py
@time: 2016/1/1 19:03
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(t)

        n = len(s)
        visited = dict()
        for chr in t:
            if chr not in visited:
                visited[chr] = 0
            else:
                visited[chr] -= 1
        start = 0
        end = 0
        min_start = 0
        min_end = n+1
        min_len = n+1
        print(min_start,min_end)
        for end in range(n):
            chr = s[end]
            if chr not in visited:
                continue
            if visited[chr] <= 0:
                m -= 1
            visited[chr] += 1
            while m == 0:
                tmp = s[start]
                if tmp not in visited:
                    start += 1
                elif visited[tmp] > 1:
                    start += 1
                    visited[tmp] -= 1
                elif visited[tmp] == 1:
                    if end - start < min_len:
                        min_start = start
                        min_end = end+1
                        min_len = end - start+1
                        print(min_start,min_end)
                    start += 1
                    visited[tmp] -= 1
                    m += 1
        print(min_start,min_end)
        if min_len == n+1:
            return ""
        else:
            return s[min_start:min_end]

A = Solution()
A.minWindow("a","aa")

