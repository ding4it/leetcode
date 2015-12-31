#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  SimplifyPath.py
@time: 2015/12/30 21:24
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        splited_path = path.split('/')
        new_path = ['' for i in range(len(splited_path))]
        k = 0
        for item in splited_path:
            if item == '':
                continue
            elif item == '.':
                continue
            elif item == '..':
                k = k -1 if k > 0 else 0
            else:
                new_path[k] = item
                k += 1
        rs = "/".join(new_path[0:k])
        return "/" + rs

A = Solution()
path = "/a/./b/../../c/"
A.simplifyPath(path)
