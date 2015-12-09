#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file: RangeSumQuery2D.py
@time: 2015/11/29 19:53
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.__matrix = matrix
        self.__row = len(matrix)
        if len(matrix) > 0:
            self.__col = len(matrix[0])
        else:
            self.__col = 0
        self.__data = [[0 for i in range(self.__col+1) ] for j in range(self.__row+1)]
        for i in range(1,self.__row+1 ):
            for j in range(1,self.__col+1):
                self.__data[i][j] = self.__data[i-1][j] + self.__data[i][j-1] - self.__data[i-1][j-1] + self.__matrix[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__data[row2+1][col2+1] - self.__data[row1][col2+1] - self.__data[row2+1][col1] +  self.__data[row1][col1]


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix)
numMatrix.sumRegion(2, 1, 4, 3)
numMatrix.sumRegion(1, 1, 2, 2)
numMatrix.sumRegion(1, 2, 2, 4)