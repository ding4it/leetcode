#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: WordPattern.py
@time: 2015/12/11 16:53
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        dictary = dict()
        sss = set()
        for i,c in enumerate(pattern):
            if dictary.get(c) == None:
                if str[i] in sss:
                    return False
                dictary[c] = str[i]
                sss.add(str[i])
            elif dictary.get(c) != str[i]:
                return False
        return True

a = Solution()
pattern = "abba"
str = "dog dog dog dog"
xx = a.wordPattern(pattern,str)
print(xx)