aclass NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self._nums = nums


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self._nums[i] = vals
        return i


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self._nums[i:j])