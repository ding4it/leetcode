#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: RemoveDuplicateLetters.py
@time: 2015/12/10 19:46
"""
import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return""
        arr = dict()
        for i,c in enumerate(s):
            arr[c] = i
        arr2 = [[k,v] for k,v in arr.items()]
        arr2 = collections.OrderedDict(sorted(arr2,key=lambda x:x[1],reverse=True))

        start = 0
        rs = []
        visited = set()
        while arr2:
            ch,end = arr2.popitem()
            tobe = 0
            while ch != tobe:
                tobe = 'z'
                k = start
                for i in range(start,end+1):
                    if s[i] < tobe and s[i] not in visited:
                        tobe = s[i]
                        k = i+1
                if ch != tobe :
                    del arr2[tobe]
                visited.add(tobe)
                rs.append(tobe)
                start = k
        return "".join(rs)



a = Solution()
s = "abacb"
a.removeDuplicateLetters(s)