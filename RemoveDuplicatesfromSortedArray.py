#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  RemoveDuplicatesfromSortedArray.py
@time: 2015/12/30 20:51
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        k = 0
        for i in range(1,n):
            if nums[k] == nums[i]:
                continue
            else:
                k += 1
                nums[k] = nums[i]
        return k+1

A = Solution()
nums = [1,1,2]
x = A.removeDuplicates(nums)
print(x)