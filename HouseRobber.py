#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: HouseRobber.py
@time: 2015/12/11 11:37
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n <3:
            return max(nums)
        arr = [0 for i in range(n)]
        arr[0]=nums[0]
        arr[1] = max(nums[0],nums[1])
        for i in range(1,n):
                arr[i] = max(arr[i-2] + nums[i],arr[i-1])
        print(arr)
        return arr[n-1]
a = Solution()
arr = [4,1,2,7,5,3,1]
a.rob(arr)