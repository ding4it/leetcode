#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: RangeSumQuery.py
@time: 2015/11/29 20:35
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.__data = [0 for i in range(n)]
        self.__data[0] = nums[0]
        for i in range(1,n):
            self.__data[i] = self.__data[i-1] +nums[i]
        print(self.__data)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i != 0:
            return self.__data[j] - self.__data[i-1]
        else:
            return self.__data[j]
nums = [-2, 0, 3, -5, 2, -1]
# Your NumArray object will be instantiated and called as such:
numArray = NumArray(nums)
a = numArray.sumRange(0, 1)
print(a)
a = numArray.sumRange(1, 2)
print(a)