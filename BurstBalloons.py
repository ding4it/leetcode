#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: BurstBalloons.py
@time: 2015/11/30 14:44
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        arr = [ [0]*n for i in range(n)]
        for k in range(2,n):
            for left in range(0,n-k):
                right = left + k
                arr[left][right] = max(arr[left][j]+ arr[j][right]+ nums[left]*nums[j]*nums[right] for j in range(left+1,right))
        print(arr[0][n-1])
        return arr[0][n-1]

a = Solution()
tt = [81,39,75,86,1,46,86,49,78,88,76,16,18,13,96,10,4,38,88,16,44,85,69,89,29,99,69,26,39,7,95,5,63,25,17,87,20,1,41,91,46,55,53,0,17,93,98,78,77,84,81,97,87,3,42,7,36,36,13,51,6,29,94,45,63,12,98,3,39,88,44,71,82,88,18,67,14,22,92,38,30,25,3,98,56,11,4,6,26,98,84,62,65,93,16,77,83,64,38,15,10,30,98,41,10,92,59,43,12,90,86,16,78,20,2,93,66,44,11,80,22,92,92,99,59,24,31,30,63,33,28,98,53,67,47,28,43,89,80,22,54,0,41,93,19,95,65,1,79,30,83,13,93,5,43,86,51,5,74,0,42,46,37,64,72,36,91,97,57,40,13,90,58,17,91,5,89,97,9,22,45,22,28,83,3,47,51,8,11,32,38,10,41,33,30,29,99,88,11,28,67,77,93,58,35,63,30,95,45,13,66,28,94,31,15,96,19,12,16,35,66,74,61,1,19,8,44,49,6,91,6,60,30,27,97,42,57,6,70,24,95,65,52,19,1,34,51,64,5,97,40,5,32,86,6,77,5,5,6,44,54,86,96,14,21,20,41,27,88,1,46,71,86,43,51,0,98,66,33,56,2,67,49,25,13,45,9,5,94,50,30,43,65,80,66,14,93,79,93,11,16]
import time
t = time.time()
a.maxCoins(tt)
print(time.time() - t)

