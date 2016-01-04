#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  NextPermutation.py
@time: 2016/1/2 15:31
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        max = 0
        i = n-1
        for i in range(n-1,0,-1):
            if nums[i] <= nums[i-1]:
                continue
            else:
                break
        if i == 1 and nums[i] <= nums[i-1]:
            nums.sort()
        else:
            minx = i
            for j in range(i+1,n):
                if nums[j] > nums[i-1] and nums[j] < nums[minx]:
                    minx = j
            nums[minx],nums[i-1] = nums[i-1],nums[minx]
            nums[i:] = sorted(nums[i:])
        print(nums)

A = Solution()
l = [3,2,1]
A.nextPermutation(l)