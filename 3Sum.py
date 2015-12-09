#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: 3Sum.py.py
@time: 2015/12/7 16:03
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        arr = set()
        if nums.count(0) >2:
            arr.add((0,0,0,))
        nums = [ nums[i] for i in range(n-2) if not nums[i] == nums[i+1] == nums[i+2]] + nums[n-2:n]
        n = len(nums)

        for i in range(n):
            if nums[i]>0 :
                break
            for j in range(i+1,n):
                if nums[i]+nums[j]>0:
                    break
                for k in range(n-1,j,-1):
                    if nums[i]+nums[j] + nums[k] < 0:
                        break
                    elif nums[i] + nums[j] + nums[k] == 0:
                        arr.add((nums[i],nums[j],nums[k],))
                        break

        arr2 = [list(x) for x in arr]
        print(arr2)
        return arr2

a = Solution()

arr =[-1,0,1]
a.threeSum(arr)