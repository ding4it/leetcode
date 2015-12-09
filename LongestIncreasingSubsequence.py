#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: LongestIncreasingSubsequence.py
@time: 2015/12/1 21:34
"""


class Solution(object):


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        arr = [1 for i in range(n)]
        search = [0 for i in range(n+1)]
        k = 1
        search[1] = nums[0]
        for i in range(1,n):
            left = 1
            right = k
            mid = (left + right)//2
            while left < right:
                mid = (left + right)//2
                if nums[i] > search[mid]:
                    left = mid + 1
                elif nums[i] == search[mid]:
                    arr[i] = mid
                    break
                else:
                    right = mid - 1
            print(left,right,nums[i],search[left])
            if nums[i] < search[left]:
                search[left] = nums[i]
                arr[i] = left
            elif nums[i] > search[left]:
                search[left+1] = nums[i]
                arr[i] = left + 1
                if left + 1 > k:
                    k = left +1
        print(arr,search,k)
        return k


a = Solution()
ttt = [10,9,2,5,3,7,101,18]
ttt = [-2,-1]
a.lengthOfLIS(ttt)