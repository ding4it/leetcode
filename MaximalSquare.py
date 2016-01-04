#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence
@contact: ding4it@gmail.com
@file:  MaximalSquare.py
@time: 2016/1/2 19:27
"""


##this algorithm is not good.
##There is a better algorithm in leetcode discuess with complecity of O(mn)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        mat = [[0]*n for i in range(m)]

        mat2 =  [[0]*n for i in range(m)]
        ok = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    ok = True
                    mat[i][j] = 1

        if not ok:
            return 0

        k = 2
        ttt = min(m,n)
        prevK = 1
        while k <= ttt:
            ok = False
            for i in range(m-k+1):
                for j in range(n-k+1):
                    mat[i][j] =  mat[i][j] & mat[i][j+prevK] & mat[i+prevK][j] & mat[i+prevK][j+prevK]
                    if mat[i][j]:
                        ok = True
            if not ok:
                break
            else:
                for i in range(m):
                    for j in range(n):
                        mat2[i][j] = mat[i][j]
                prevK = k
                k *= 2
        mat = mat2
        for i in mat:
            print(i)
        prevK = prevK//2
        k = k//2
        start = k
        end = min(ttt,2*k-1)
        print("hereeee", start,end,2*prevK)
        if start == end:
            return start*start
        while start <= end:
            mid = (start + end)//2
            ok = False
            for i in range(m-mid+1):
                if ok:
                    break
                for j in range(n-mid+1):
                    step = mid - 2*prevK
                    tmp =  mat[i][j] & mat[i][j+step] & mat[i+step][j] & mat[i+step][j+step]
                    if tmp:

                        ok = True
                        break
            if ok:
                start = mid + 1
            else:
                end = mid -1
        print("return ", start,end)
        return end*end
A = Solution()
m =["0010","1111","1111","1110","1100","1111","1110"]
x = A.maximalSquare(m)
print(x)



# class Solution(object):
#     def maximalSquare(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         m = len(matrix)
#         if m == 0:
#             return 0
#         n = len(matrix[0])
#         mat = [[0]*n for i in range(m)]
#         ok = False
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == '1':
#                     ok = True
#                     mat[i][j] = 1
#
#         if not ok:
#             return 0
#         k = 1
#         ttt = min(m,n)
#         for k in range(1,ttt):
#             ok = False
#             for i in range(m-k):
#                 for j in range(n-k):
#                     mat[i][j] =  mat[i][j] & mat[i][j+1] & mat[i+1][j] & mat[i+1][j+1]
#                     if mat[i][j]:
#                         ok = True
#             if not ok:
#                 return k*k
#         return ttt * ttt