#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  RemoveElement.py
@time: 2016/3/8 22:53
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[p] = nums[i]
                p = p+1
        return p
